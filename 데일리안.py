import requests
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from urllib import parse
import sys

daily_urls = []
f=open("데일리안.txt", 'w', encoding="UTF-8")

for i in range(1, 4):
    url = "https://dailian.co.kr/itScience?page=" + str(i)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.content, "lxml")
    links = soup.select('div.wide1Box > a')
    for link in links:
        daily_urls.append("https://dailian.co.kr" + link['href'])
        #print(daily_urls)
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
    """ print(title)
    print(date)
    print(content)
    print(author.text) """

        
