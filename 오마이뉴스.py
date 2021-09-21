import requests
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from urllib import parse
import sys

oh_urls = []
f=open("오마이뉴스.txt", 'w', encoding="UTF-8")

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
    #content = soup.select_one('div.at_contents > strong')
    """ print(title)
    print(author)
    print(date)
    print(content) """