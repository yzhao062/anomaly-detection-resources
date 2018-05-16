#!/usr/bin/python

"""
    This script will download all papers/books and rename to proper name
    if there is no copyright issue.

    TODO: download resources by item number
    TODO: add exception handler for downloader
"""
import re
import pathlib
import urllib.request

# initialize the log directory if it does not exist
pathlib.Path('resources').mkdir(parents=True, exist_ok=True)

f = open('resource_urls\\papers.txt', 'r')
for line in f:
    # print(line)
    line_splits = line.split(' | ')

    # remove all special char in file name
    file_name = re.sub(r'[\\/*?:"<>|]', "", line_splits[0])
    # strip filename length in case it is too long
    if len(file_name) > 255:
        file_name = file_name[:255]
    url = line_splits[1]

    print('Downloading', file_name, 'from', url)
    urllib.request.urlretrieve(url, "resources\\" + file_name + '.pdf')

f.close()
