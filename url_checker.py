import re
import requests


def exists(path):
    """ Utility function to check whether a web file exists
    :param path:
    :return:
    """
    r = requests.head(path)
    # print(r.status_code)
    return r.status_code == requests.codes.ok


def exists_adv(path):
    """ Utility function to check whether a web file exists
    :param path:
    :return:
    """
    # TODO: use selenium
    r = requests.head(path)
    # print(r.status_code)
    return r.status_code == requests.codes.ok


if __name__ == "__main__":
    # driver = webdriver.Firefox()
    manual_links = []
    potential_broken_links = []
    with open('README_11232019.md', encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        result = re.search(']\(http(.*)\)', line)
        if result:
            link = "http" + result.group(1)
            if "github" in link or "coursera" in link:
                manual_links.append(link)
            else:
                flag = exists(link)
                if not flag:
                    potential_broken_links.append(link)
                    print(link)

    print()
    for link in manual_links:
        print(link)
