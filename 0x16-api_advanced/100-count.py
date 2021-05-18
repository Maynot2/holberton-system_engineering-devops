#!/usr/bin/python3

"""
    Queries the Reddit API
"""

import requests


def count_same_word(text, word):
    """Counts how many repeated given word in text"""
    count = 0
    words = text.strip().split(" ")
    for w in words:
        if w.lower() == word:
            count += 1
    return count


def count_words_rec(subreddit, word_dict, hot_list=[], after=None):
    """Returns the number hot posts for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'APIadvanced/0.0.1'}
    payload = {'limit': 100, 'after': after}
    request = requests.get(url, allow_redirects=False, headers=headers,
                           params=payload)

    if request.status_code == 200:
        next_page = request.json().get('data').get('after')
        children = request.json().get('data').get('children')
        for child in children:
            title = child.get('data').get('title')
            for word in word_dict.keys():
                word_dict[word] += count_same_word(title, word)
        if next_page:
            return count_words_rec(subreddit, word_dict, hot_list, next_page)
        return word_dict


def count_words(subreddit, word_list):
    """Wrapper function for recursive call"""
    word_dict = {}
    for word in word_list:
        word_dict[word] = 0
    w_d = count_words_rec(subreddit, word_dict)
    if w_d:
        sorted_list = sorted(w_d.items(), key=lambda x: x[1], reverse=True)
        for word, count in sorted_list:
            if count > 0:
                print('{} : {}'.format(word, count))
