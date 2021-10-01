import requests
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from urllib import parse
import sys
import os

# 오마이뉴스 > 코인리더스 > 데일리안 순서
print("Web Crawling start")

# 오마이뉴스 구역
oh_urls = []
# filepath = "../../../_INDEXDB/set2/WEB/dat/"
# scd_path = sys.argv(1)
# print("scd path : " + scd_path)
# file_path = sys.argv[1].replace(':', ':/')
file_path = sys.argv[1][:-3]
print("file path : " + file_path)
f=open(file_path + '/result.scd', 'w', encoding='UTF-8')
#f=open("C:/awsKey/result.scd", 'w', encoding="UTF-8")

for i in range(1, 4):
    url = "http://www.ohmynews.com/NWS_Web/Articlepage/Total_Article.aspx?PAGE_CD=C0300&pageno=" + str(i)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.content, "lxml")
    links = soup.select('div.cont > dl > dt > a')
    for link in links:
        oh_urls.append("http://www.ohmynews.com" + link['href'])
for oh_url in (oh_urls):
    url = oh_url
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.content, "lxml")

    title = soup.find('meta', {'property': 'og:title'}).get('content')
    date = soup.find('meta', {'property': 'article:published_time'}).get('content')
    author = soup.find('meta', {'property':'dable:author'}).get('content')
    content = soup.find('meta', {'property':'og:description'}).get('content')
    
    f.write('^MA_TITLE:'+ title + '\n')
    f.write('^DDJ:' + author + '\n')
    f.write('^REG_DATE:' + date + '\n')
    f.write('^MA_DESC:' + content + '\n')
print("Oh-my news done")

# 코인리더스 구역
coin_urls = []

# 200 : 정상
for i in range(1, 4):
    url = "https://www.coinreaders.com/sub.html?page=" + str(i) + "&section=sc10&section2="
    res=requests.get(url)
    # 만약 문제가 있다면 즉시 종료한다
    res.raise_for_status()
    #print("응답코드 :", res.status_code)

    # 가져온 html 문서를 lxml parser를 통해서 beautifulsoup 객체로 만듦
    soup=BeautifulSoup(res.content, "lxml")

    links = soup.select('div.sub_read_list_box > dl > dt > a')
    for link in links:
        coin_urls.append("https://www.coinreaders.com" + link['href'])

for coin_url in (coin_urls):
    url = coin_url
    res=requests.get(url)
    soup=BeautifulSoup(res.content, "lxml")

    name = soup.select_one('div.article_head > h1')
    author = soup.find('meta', {'property':'dable:author'}).get('content')
    date = soup.find('meta', {'property':'article:published_time'}).get('content')
    content = soup.select_one('#textinput > p')

    f.write('^MA_TITLE:'+ name.text + '\n')
    f.write('^DDJ:' + author + '\n')
    f.write('^REG_DATE:' + date + '\n')
    f.write('^MA_DESC:' + content.text + '\n')
print("coin readers done")
    
# 데일리안 구역
daily_urls = []

for i in range(1, 4):
    url = "https://dailian.co.kr/itScience?page=" + str(i)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.content, "lxml")
    links = soup.select('div.wide1Box > a')
    for link in links:
        daily_urls.append("https://dailian.co.kr" + link['href'])
        
for daily_url in (daily_urls):
    url = daily_url
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml")
    title = soup.find('meta', {'property': 'og:title'}).get('content')
    date = soup.find('meta', {'property': 'article:published_time'}).get('content')
    content = soup.find('meta', {'property': 'og:description'}).get('content')
    author = soup.select_one('div.reportText > div > b')
    f.write('^MA_TITLE:'+ title + '\n')
    f.write('^DDJ:' + author.text + '\n')
    f.write('^REG_DATE:' + date + '\n')
    f.write('^MA_DESC:' + content + '\n')
print("daily ahn done")
f.close()

print("done")