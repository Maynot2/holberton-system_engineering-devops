#!/usr/bin/python3

"""
    Queries the Reddit API
"""

import requests


def add_title_rec(hot_list, children, index, limit):
    """Adds title to the hot_list recursively"""
    if index == limit - 1:
        return hot_list
    hot_list.append(children[index].get('title'))
    return add_title_rec(hot_list, children, index + 1, limit)


def all_hot_titles_rec(subreddit, hot_list=[], after=None):
    """Returns the number hot posts for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'APIadvanced/0.0.1'}
    payload = {'limit': 100, 'after': after}
    request = requests.get(url, allow_redirects=False, headers=headers,
                           params=payload)

    if request.status_code == 200:
        next_page = request.json().get('data').get('after')
        children = request.json().get('data').get('children')
        add_title_rec(hot_list, children, 0, len(children))
        if next_page:
            return all_hot_titles_rec(subreddit, hot_list, next_page)
        return hot_list


def recurse(subreddit, hot_list=[]):
    """Wrapper function for recursive call"""
    return all_hot_titles_rec(subreddit, hot_list)
