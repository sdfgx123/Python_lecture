import requests
from bs4 import BeautifulSoup
import sys
# scd 파일 생성 / 위치 : 파이썬 설치 경로
f=open("test_11th.scd", 'w')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
url = "http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791165343729"
r = requests.get(url, headers=headers)
r.status_code
soup = BeautifulSoup(r.text, 'html.parser')
book_info = soup.find_all('div', class_='detail')
title=[]
subtitle=[]
author=[]
for info in book_info:
    tmp_title=info.find('a')
    tmp_subtitle=info.find('div', class_="subtitle")
    title=tmp_title.find('strong')
    res="^title: "+title.get_text()+"\n"
    f.write(res)
    f.write("^content: "+tmp_subtitle.get_text().strip()+"\n")
    print('\n')
f.close()