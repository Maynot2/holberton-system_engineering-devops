#!/usr/bin/python3

"""
    Queries the Reddit API
"""

import requests
import json


def top_ten(subreddit):
    """Prints the title of the top 10 hot posts listed for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/top.json'.format(subreddit)
    headers = {'User-Agent': 'APIadvanced/0.0.1'}
    payload = {'limit': 10}
    request = requests.get(url, allow_redirects=False, headers=headers,
                           params=payload)

    if request.status_code == 200:
        for post in request.json().get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
