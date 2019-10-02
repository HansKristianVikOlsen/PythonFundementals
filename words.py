#!/usr/bin/env python3
""""Retreive and prints words from Url

Usage:
    python3 words.py <Url>
"""

from urllib.request import urlopen
import sys

# http://sixty-north.com/c/t.txt


def fetch_words(url):
    """Fetch a list of words from a url

    args:
        url

    Returns:
        A list of strings containign the words from the url

    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """

    args:


    Returns:

    """
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
