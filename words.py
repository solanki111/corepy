"""
Retrieve and print words from a URL.

Usage:

    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen

def fetch_words():
    """
    Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    :return: A list of strings containing the words from
        the document.
    """
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """
    Print items one per line.

    :param items: An iterable series of printable items.
    :return: Prints the items.
    """
    for item in items:
        print(item)


def main(url):
    """
    Print each word from a text document from at a URL.

    :param url: The URL of a UTF-8 text document.

    :return: None
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])