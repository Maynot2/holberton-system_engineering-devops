#!/usr/bin/python3
"""
    Fetches data from jsonplaceholder API
"""

import csv
import requests
from sys import argv


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
        format_todos(todos, username)
        file_name = '{}.csv'.format(id_num)
        with open(file_name, "w") as outfile:
            writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
            for todo in todos:
                writer.writerow([
                        id_num, todo.get('username'),
                        todo.get('completed'),
                        todo.get('task')
                    ])
