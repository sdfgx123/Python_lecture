# Inflearn 파이썬 크롤링 테스트
import requests
from bs4 import BeautifulSoup
import sys
f=open("test_5th.scd", 'w')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
url = "http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79"
r = requests.get(url, headers=headers)
r.status_code
soup = BeautifulSoup(r.text, 'html.parser')
book_info = soup.find_all('div', class_='detail')
title=[]
subtitle=[]
author=[]
for info in book_info:
    tmp=info.find('a')
    title=tmp.find('strong')
    res="^title: "+title.get_text()
    f.write(res)
    print('\n')
f.close()