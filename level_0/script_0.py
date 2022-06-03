#!/usr/bin/python3
import requests

url = 'http://158.69.76.135/level0.php'
data_to_send = {'id': '4256', 'holdthedoor': 'submit'}
for i in range(1024):
    r = requests.post(url, data=data_to_send)
