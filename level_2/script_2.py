#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

url = 'http://158.69.76.135/level2.php'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                        'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                        'Chrome/74.0.3729.169 Safari/537.36', 'referer': url}

for i in range(1024):
    s = requests.Session()
    rep = s.get(url, headers=header)

    soup = BeautifulSoup(rep.text, 'html.parser')
    key = soup.find(type='hidden')["value"]
    data_to_send = {'id': '4256',
                    'holdthedoor': 'submit',
                    'key': key}

    s.post(url, data=data_to_send, headers=header)
