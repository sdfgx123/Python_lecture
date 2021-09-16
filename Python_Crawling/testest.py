import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib import parse
import sys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)


# 연합뉴스
url = "https://www.yna.co.kr/economy/finance?site=navi_economy_depth02"

driver.get(url)
crObject = BeautifulSoup(driver.page_source, 'html.parser')

yna_urls = []
for a in crObject.find_all('a', href=True, attrs={'class':'tit-wrap'}):
    link = "https:" + a['href']
    yna_urls.append(link)
    print(link)

for yna_url in (yna_urls):

    driver.get(yna_url)
    crObject = BeautifulSoup(driver.page_source, 'html.parser')

    title = crObject.find('meta', {'property':'og:title'}).get('content')[:-7]
    author = crObject.find('meta', {'property':'article:author'}).get('content')
    date = crObject.find('meta', {'property':'article:published_time'}).get('content')
    content = crObject.select('article.story-news article > p')[0].get_text()

    print('^MA_TITLE:'+title,'^MA_DESC:'+content,'^DDJ:'+author,'^REG_DATE:'+date,sep='\n')