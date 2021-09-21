import requests
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from urllib import parse
import sys

yna_urls = []

for i in range(1, 4):
    url = "https://www.yna.co.kr/economy/real-estate/" + str(i)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.content, "lxml")
    links = soup.select('div.news-con > a')
    for link in links:
        yna_urls.append("https:" + link['href'])

for yna_url in (yna_urls):
    url = yna_url
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml")
    title = soup.find('meta', {'property':'og:title'}).get('content')
    author = soup.find('meta', {'property':'article:author'}).get('content')
    date = soup.find('meta', {'property':'article:published_time'}).get('content')
    #content = soup.select_one('div.scroller01 > p:nth-child(3)').text
    content = soup.find('article', {'class':'story-news article'}).find('p').text.strip()
    print(title[:-7])
    print(author)
    print(date)
    print(content)
    #print(soup.select_one("li:nth-child(5)").string)
    #text = crObject.find('article', {'class':'story-news article'}).find('p').text.strip()