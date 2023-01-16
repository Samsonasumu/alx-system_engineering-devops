#!/usr/bin/python3
"""Uses https://jsonplaceholder.typicode.com"""
import csv
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
    with open('{}.csv'.format(sys.argv[1]), mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for i, e in enumerate(titles):
            writer.writerow([user_id, name, completed[i], e])
