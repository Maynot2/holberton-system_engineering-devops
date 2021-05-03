#!/usr/bin/python3
"""
    Fetches data from jsonplaceholder API
"""

from sys import argv
import json
import requests


def format_todos(todos, name):
    for todo in todos:
        todo['task'] = todo.pop('title')
        todo.pop("userId")
        todo.pop("id")
        todo['username'] = name

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
        username = r1.json().get('username')
        todos = r2.json()
        record = {}
        format_todos(todos, username)
        record[id_num] = todos
        file_name = '{}.json'.format(id_num)
        with open(file_name, "w") as outfile:
            json.dump(record, outfile)
