#!/usr/bin/env python3

"""
Robust URL checker for README-style reStructuredText documents.

Features:
1. Extracts and cleans HTTP/HTTPS links from text.
2. Removes common trailing punctuation from RST/Markdown contexts.
3. Uses retries and a browser-like User-Agent.
4. Falls back from HEAD to GET for servers that reject HEAD.
5. Checks links concurrently and prints a final summary.

Usage:
    python url_checker.py
    python url_checker.py --file README_CN.rst --timeout 8 --workers 20
"""

from __future__ import annotations

import argparse
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Iterable
from urllib.parse import urlsplit, urlunsplit

import requests
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

TRAILING_PUNCT = set('`">),.;:_]')
DEFAULT_TIMEOUT = 8
DEFAULT_WORKERS = 16


@dataclass(frozen=True)
class CheckResult:
    url: str
    ok: bool
    status_code: int | None
    method: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check URLs from an RST file.")
    parser.add_argument(
        "--file",
        default="README.rst",
        help="RST/Markdown file to parse (default: README.rst).",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"Request timeout in seconds (default: {DEFAULT_TIMEOUT}).",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=DEFAULT_WORKERS,
        help=f"Number of parallel workers (default: {DEFAULT_WORKERS}).",
    )
    parser.add_argument(
        "--show-ok",
        action="store_true",
        help="Also print successful URLs.",
    )
    return parser.parse_args()


def clean_url(raw_url: str) -> str:
    url = raw_url.strip()
    while url and url[-1] in TRAILING_PUNCT:
        url = url[:-1]

    # Rebuild URL to normalize casing for host and remove fragment-only noise.
    parts = urlsplit(url)
    netloc = parts.netloc.lower()
    fragment = ""
    cleaned = urlunsplit((parts.scheme, netloc, parts.path, parts.query, fragment))
    return cleaned


def extract_urls(content: str) -> list[str]:
    # Match until whitespace; cleanup handles RST trailing characters.
    raw_urls = re.findall(r"https?://\S+", content)
    cleaned = set()
    for raw_url in raw_urls:
        normalized = clean_url(raw_url)
        if normalized:
            cleaned.add(normalized)
    return sorted(cleaned)


def build_session() -> Session:
    retry = Retry(
        total=2,
        connect=2,
        read=2,
        backoff_factor=0.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"HEAD", "GET"}),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry)

    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (compatible; URLChecker/2.0; +https://github.com/yzhao062/"
                "anomaly-detection-resources)"
            )
        }
    )
    return session


def should_fallback_to_get(status_code: int) -> bool:
    return status_code in (403, 405, 406, 429, 500, 501, 502, 503)


def check_one_url(url: str, timeout: int) -> CheckResult:
    session = build_session()
    try:
        head_resp = session.head(url, allow_redirects=True, timeout=timeout)
        if head_resp.status_code < 400:
            return CheckResult(url, True, head_resp.status_code, "HEAD", "OK")

        if should_fallback_to_get(head_resp.status_code):
            get_resp = session.get(url, allow_redirects=True, timeout=timeout, stream=True)
            # Avoid downloading full body.
            get_resp.close()
            if get_resp.status_code < 400:
                return CheckResult(url, True, get_resp.status_code, "GET", "OK (fallback)")
            return CheckResult(
                url,
                False,
                get_resp.status_code,
                "GET",
                f"Fallback failed after HEAD {head_resp.status_code}",
            )

        return CheckResult(url, False, head_resp.status_code, "HEAD", "HTTP error")
    except requests.RequestException as exc:
        return CheckResult(url, False, None, "HEAD/GET", f"RequestException: {exc}")
    finally:
        session.close()


def check_all(urls: Iterable[str], timeout: int, workers: int) -> list[CheckResult]:
    results: list[CheckResult] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(check_one_url, url, timeout): url for url in urls}
        for future in as_completed(futures):
            results.append(future.result())
    return sorted(results, key=lambda r: r.url)


def main() -> int:
    args = parse_args()
    try:
        with open(args.file, "r", encoding="utf-8") as handle:
            content = handle.read()
    except FileNotFoundError:
        print(f"Error: file not found: {args.file}")
        return 2

    urls = extract_urls(content)
    if not urls:
        print(f"No URLs found in {args.file}.")
        return 0

    print(f"Found {len(urls)} unique URLs in {args.file}. Checking...")
    results = check_all(urls, timeout=args.timeout, workers=max(1, args.workers))

    ok_count = 0
    fail_count = 0
    for result in results:
        if result.ok:
            ok_count += 1
            if args.show_ok:
                print(f"[OK]   {result.url} [{result.method} {result.status_code}]")
            continue
        fail_count += 1
        status = result.status_code if result.status_code is not None else "N/A"
        print(f"[FAIL] {result.url} [{result.method} {status}] {result.detail}")

    print()
    print(f"Summary: total={len(results)} ok={ok_count} fail={fail_count}")
    return 1 if fail_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
