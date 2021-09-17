import requests
from bs4 import BeautifulSoup
import sys

# 200 : 정상
url="https://www.coinreaders.com/sub.html?page=1&section=sc10&section2="
res=requests.get(url)
# 만약 문제가 있다면 즉시 종료한다
res.raise_for_status()
#print("응답코드 :", res.status_code)

# 가져온 html 문서를 lxml parser를 통해서 beautifulsoup 객체로 만듦
soup=BeautifulSoup(res.content, "lxml")

#print(soup.title.get_text())
#print(soup.find('div dl dt a', {'class':'sub_read_list_box'}).get_text())

print(soup.select('div.sub_read_list_box > dl > dt')[0].text) # 기사 제목만 가져옴

titles = soup.select('div.sub_read_list_box > dl > dt') # 기사 제목들 가져오기
for title in titles:
    print(title.text)

print(soup.select('div.sub_read_list_box > dl > dt > a')[0]['href']) # 기사 링크

links = soup.select('div.sub_read_list_box > dl > dt > a')
for link in links:
    print(link['href'])