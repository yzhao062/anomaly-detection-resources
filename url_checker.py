#!/usr/bin/env python3

"""
Script: check_urls_in_readme.py

Place this script in the same folder as README.rst. When you run it,
it will search for all HTTP/HTTPS links in README.rst and attempt
to connect via a HEAD request. Any inaccessible links will be flagged.

Usage:
    python check_urls_in_readme.py
"""

import re
import requests

# Characters we often see trailing links in reStructuredText
# e.g.,  https://arxiv.org/abs/2309.15376>`_ or  ) or .
# We iterate from the end of the string and remove them until
# the last character is no longer in this set.
TRAILING_PUNCT = set('`">),._')

def clean_url(url: str) -> str:
    """
    Iteratively strip from the right any of the punctuation
    chars in TRAILING_PUNCT, often appearing in RST link syntax.
    """
    while url and url[-1] in TRAILING_PUNCT:
        url = url[:-1]
    return url

def main():
    filename = 'README.rst'  # Adjust if your RST file has another name

    # Read the RST file
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find {filename}. Please place this script in "
              f"the same directory as {filename}.")
        return

    # Regex to match http:// or https:// until whitespace or newline
    url_pattern = re.compile(r'http[s]?://\S+')
    raw_urls = url_pattern.findall(content)

    # Clean up trailing punctuation for each raw URL
    urls = set(clean_url(u) for u in raw_urls)

    if not urls:
        print("No URLs found in the file.")
        return

    # Check each URL
    for url in sorted(urls):
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            if response.status_code < 400:
                print(f"[OK]    {url}")
            else:
                print(f"[FAIL]  {url} (Status code: {response.status_code})")
        except requests.RequestException as e:
            print(f"[FAIL]  {url} (Exception: {e})")

if __name__ == "__main__":
    main()
