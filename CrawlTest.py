# Inflearn 파이썬 크롤링 테스트
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
url = "https://finance.naver.com/item/board.nhn?code=263800"

r = requests.get(url, headers=headers)
r.status_code

soup = BeautifulSoup(r.text, 'html.parser')

title = soup.find_all('td', class_='title')
for i in title:
    print(i.text)