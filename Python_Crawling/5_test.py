import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/index"
res=requests.get(url)

# 의미 : 가져온 html 문서를 lxml parser를 통해서 beautifulsoup 객체로 만듦
soup=BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# a element의 속성 정보
# print(soup.a.attrs)
# 원하는 속성값만 반환
# print(soup.a["href"])
# soup 객체에서, a 태그에서, class가 Nbtn_upload인 element만 반환
# print(soup.find("a", attrs={"class": "Nbtn_upload"}))
rank1=soup.find("li", attrs={"class":"rank01"})
print(rank1.a)