#!/usr/bin/python3
"""
    Fetches data from jsonplaceholder API
"""

import json
import requests
from sys import argv


def format_todos(todos, name):
    """format todo list to requierement"""
    for todo in todos:
        todo['task'] = todo.pop('title')
        todo.pop("userId")
        todo.pop("id")
        todo['username'] = name


if __name__ == "__main__":
    r1 = requests.get('https://jsonplaceholder.typicode.com/users')
    users = r1.json()
    records = {}
    for user in users:
        id_num = user.get('id')
        r2 = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}/todos'
                .format(id_num)
            )
        username = user.get('username')
        todos = r2.json()
        format_todos(todos, username)
        records[id_num] = todos
    with open('todo_all_employees.json', 'w') as outfile:
        json.dump(records, outfile)
