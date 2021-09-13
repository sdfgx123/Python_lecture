import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text, "lxml")
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a) # 처음 발견되는 a
#print(soup.a.attrs) 딕셔너리 형태로 반환
print(soup.a["href"])
