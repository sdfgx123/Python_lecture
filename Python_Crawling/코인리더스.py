from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib import parse
import sys

# page=1부터 page=3까지 반복
for i in range(1, 4):
    url="http://tvdaily.asiae.co.kr/section.html?section=2&page=" + str(i)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(30) #브라우저에서 사용되는 엔진 자체에서 파싱되는 시간을 기다려주는 메소드

    # 네이버의 베스트셀러 웹페이지를 가져온다.
    driver.get(url)
    crObject = BeautifulSoup(driver.page_source, 'html.parser')

    news_urls = []
    for a in crObject.find_all('a', href=True, attrs={'class':'secttl'}):
        print(a['href'])
        news_urls.append(a['href'])
    
    for news_url in (news_urls):
        driver.get(news_urls)
        crObject = BeautifulSoup(driver.page_source, 'html.parser')

        title=crObject.find('title')
        print(title)

