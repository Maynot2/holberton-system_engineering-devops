#!/usr/bin/python3
"""
    Fetches data from jsonplaceholder API
"""

from sys import argv
from json import load
import requests


if __name__ == "__main__":
    if len(argv) == 2:
        id_num = argv[1]
        r1 = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}'
                .format(id_num)
            )
        r2 = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}/todos'
                .format(id_num)
            )
        name = r1.json().get('name')
        todos = r2.json()
        completed = []
        for todo in todos:
            if todo.get('completed'):
                completed.append(todo)
        print('Employee {} is done with tasks({}/{}):'.format(name,
                                                              len(completed),
                                                              len(todos)))
        for todo in completed:
            print('\t {}'.format(todo.get('title')))
