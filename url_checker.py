import re
import requests


def exists(path):
    """ Utility function to check whether a web file exists
    :param path:
    :return:
    """
    r = requests.head(path)
    return r.status_code == requests.codes.ok


if __name__ == "__main__":
    with open('README.md', encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        result = re.search(']\(http(.*)\)', line)
        if result:
            link = "http" + result.group(1)
            print(link, exists(link))
