#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

url = 'http://158.69.76.135/level1.php'

for i in range(4096):
    s = requests.Session()
    rep = s.get(url)

    soup = BeautifulSoup(rep.text, 'html.parser')
    key = soup.find(type='hidden')["value"]
    data_to_send = {'id': '4256',
                    'holdthedoor': 'submit',
                    'key': key}

    s.post(url, data=data_to_send)
