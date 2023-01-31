#!/usr/bin/python3
"""parses the title of all hot articles, and prints a sorted
count of given keywords"""
import requests
import re


def count_words(subreddit, word_list, hot_list=[], after=None):
    """parses the title of all hot articles"""
    URL = 'http://reddit.com/r/{}/hot.json'.format(subreddit)
    HEADERS = {'User-agent': 'Unix:0-subs:v1'}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return print_results(word_list, hot_list)

    response = requests.get(URL, headers=HEADERS, params=params)
    posts = response.json().get('data', {}).get('children', {})
    if response.status_code != 200 or not posts:
        return None
    data = response.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return count_words(subreddit, word_list, hot_list, after)


def print_results(word_list, hot_list):
    '''Prints'''
    count = {}
    for word in word_list:
        count[word] = 0
    for title in hot_list:
        for word in word_list:
            count[word] = count[word] +\
             len(re.findall(r'(?:^| ){}(?:$| )'.format(word), title, re.I))

    count = {k: v for k, v in count.items() if v > 0}
    words = sorted(list(count.keys()))
    for word in sorted(words,
                       reverse=True, key=lambda k: count[k]):
        print("{}: {}".format(word, count[word]))
