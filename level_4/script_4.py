#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

url = 'http://158.69.76.135/level4.php'
proxy_url = 'https://free-proxy-list.net/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                        'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                        'Chrome/74.0.3729.169 Safari/537.36', 'referer': url}

i = 0
while i < 98:
    s = requests.Session()
    pro = s.get(proxy_url)
    soup = BeautifulSoup(pro.text, 'html.parser')
    proxy_list = soup.find("tbody").find_all("tr")

    for p in proxy_list:
        proxy = {'http': 'http://' + str(p.find("td").text)}
        try:
            rep = s.get(url, headers=header)
            soup = BeautifulSoup(rep.text, 'html.parser')
            key = soup.find(type='hidden')["value"]

            data_to_send = {'id': '4256',
                            'holdthedoor': 'submit',
                            'key': key}

            s.post(url, data=data_to_send, headers=header, proxies=proxy, timeout=5)
            total = list(soup.find_all("td"))
            for j in range(len(total)):
                if "4256" in str(total[j].text):
                    if i < int(total[j + 1].text):
                        i = int(total[j + 1].text)
                        print(i)
                        if i == 98:
                            break
                    else:
                        print("fail")
        except:
            print("fail")
