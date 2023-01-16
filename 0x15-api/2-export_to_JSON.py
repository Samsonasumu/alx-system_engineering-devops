#!/usr/bin/python3
"""Uses https://jsonplaceholder.typicode.com"""
import json
import requests
import sys


if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
    d = r.json()
    name = d.get('username')
    user_id = d.get('id')
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    d_todos = r.json()
    titles = []
    completed = []
    for i in d_todos:
        if i.get('userId') == user_id:
            titles.append(i.get('title'))
            completed.append(i.get('completed'))
    l = [{'username': name, 'completed': completed[i], 'task': e}
         for i, e in enumerate(titles)]
    json_dict = {user_id: l}
    with open('{}.json'.format(sys.argv[1]), mode='w') as json_file:
        json.dump({user_id: l}, json_file)
