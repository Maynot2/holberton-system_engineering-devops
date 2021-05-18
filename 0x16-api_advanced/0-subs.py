#!/usr/bin/python3

"""
    Queries the Reddit API
"""

import requests
import json


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""

    url = 'https://www.reddit.com//r/{}/about.json'.format(subreddit)
    headers = { 'User-Agent': 'APIadvanced/0.0.1'}
    request = requests.get(url, allow_redirects=False, headers=headers)

    if request.status_code == 200:
        return request.json().get('data').get('subscribers')
    else:
        return 0;
