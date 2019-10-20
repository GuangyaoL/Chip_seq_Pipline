#! -*- utf-8 -*-
import requests
res = requests.get('http://127.0.0.1:8050/')
res.encoding = 'utf-8'
with open('tmp.html','w')as fw:
    for line in res.text:
        fw.write(line)
