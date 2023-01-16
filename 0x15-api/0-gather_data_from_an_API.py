#!/usr/bin/python3
"""Uses https://jsonplaceholder.typicode.com"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
    d = r.json()
    name = d.get('name')
    user_id = d.get('id')
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    d_todos = r.json()
    tasks, completed = 0, 0
    titles = []
    for i in d_todos:
        if i.get('userId') == user_id:
            tasks += 1
            if i.get('completed'):
                completed += 1
                titles.append(i.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, tasks))
    for i in titles:
        print('\t', i)
