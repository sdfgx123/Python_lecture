from logging import exception
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib import parse
import sys

try:
    f=open("crawl.txt", 'w', encoding="UTF-8")

    url = "https://book.naver.com/bestsell/bestseller_list.nhn?cp=conects"

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(30) #브라우저에서 사용되는 엔진 자체에서 파싱되는 시간을 기다려주는 메소드

    # 네이버의 베스트셀러 웹페이지를 가져온다.
    driver.get(url)
    crObject = BeautifulSoup(driver.page_source, 'html.parser')

    # 책의 상세 웹페이지 주소를 추출하여 리스트에 저장한다.
    book_page_urls = []
    for index in range(0, 25): #상세페이지 방문 횟수
        dl_data = crObject.find('dt', {'id':"book_title_"+str(index)})
        link = dl_data.select('a')[0].get('href')
        book_page_urls.append(link)

    # 메타 정보와 본문에서 필요한 정보를 추출한다.
    for book_page_url in (book_page_urls):

        driver.get(book_page_url)
        crObject = BeautifulSoup(driver.page_source, 'html.parser')

        title = crObject.find('meta', {'property':'og:title'}).get('content')
        author = crObject.find('dt', text='저자').find_next_siblings('dd')[0].text.strip()
        date = crObject.find('dt', text='출판일').find_next_siblings('dd')[0].text.strip()
        text = crObject.find('div', {'id':'bookIntroContent'}).find('p').text.strip()
        #print('^MA_TITLE:'+title,'^MA_DESC:'+text,'^DDJ:'+author,'^REG_DATE:'+date,sep='\n')
        #f.write('^MA_TITLE:'+title,'^MA_DESC:'+text,'^DDJ:'+author,'^REG_DATE:'+date,sep='\n')
        f.write('^MA_TITLE:'+title+'\n')
        f.write('^MA_DESC:'+text+'\n')
        f.write('^DDJ:'+author+'\n')
        f.write('^REG_DATE:'+date+'\n')

    # 세계일보
    url = "https://www.segye.com/newsList/0101030300000"

    driver.get(url)
    crObject = BeautifulSoup(driver.page_source, 'html.parser')

    segye_urls = []
    for a in crObject.find_all('a', href=True, attrs={'target':'_self'}):
        link = "https://www.segye.com" + a['href']
        type(link)
        segye_urls.append(link)
        print(link)

    for segye_url in (segye_urls):

        driver.get(segye_url)
        crObject = BeautifulSoup(driver.page_source, 'html.parser')

        title = crObject.find('meta', {'property':'og:title'}).get('content')
        author = crObject.find('meta', {'property':'dd:author'}).get('content')
        date = crObject.find('meta', {'property':'article:published_time'}).get('content')
        text = crObject.find('article', {'class':'viewBox'}).find('p').text.strip()
        #date = crObject.find('meta', {'property':'article:published_time'}).get('content')
        #author = re.findall('^[.+?:',crObject.find('meta', {'property':'og:description'}).get('content'))
        #print("뉴스 타이틀:", title)
        #print("title:", title)
        #f.write('^MA_TITLE:'+title,'^MA_DESC:'+text,'^DDJ:'+author,'^REG_DATE:'+date,sep='\n')
        f.write('^MA_TITLE:'+title+'\n')
        f.write('^MA_DESC:'+text+'\n')
        f.write('^DDJ:'+author+'\n')
        f.write('^REG_DATE:'+date+'\n')

        print('^MA_TITLE:'+title,'^MA_DESC:'+text,'^DDJ:'+author,'^REG_DATE:'+date,sep='\n')

    # 연합뉴스
    url = "https://www.yna.co.kr/economy/finance?site=navi_economy_depth02"

    driver.get(url)
    crObject = BeautifulSoup(driver.page_source, 'html.parser')

    yna_urls = []
    for a in crObject.find_all('a', href=True, attrs={'class':'tit-wrap'}):
        link = "https:" + a['href']
        yna_urls.append(link)

    for yna_url in (yna_urls):

        driver.get(yna_url)
        crObject = BeautifulSoup(driver.page_source, 'html.parser')

        title = crObject.find('meta', {'property':'og:title'}).get('content')[:-7]
        author = crObject.find('meta', {'property':'article:author'}).get('content')
        date = crObject.find('meta', {'property':'article:published_time'}).get('content')
        text = crObject.find('article', {'class':'story-news article'}).find('p').text.strip()
        #f.write('^MA_TITLE:'+title,'^MA_DESC:'+text,'^DDJ:'+author,'^REG_DATE:'+date,sep='\n')
        f.write('^MA_TITLE:'+title+'\n')
        f.write('^MA_DESC:'+text+'\n')
        f.write('^DDJ:'+author+'\n')
        f.write('^REG_DATE:'+date+'\n')

        #print('^MA_TITLE:'+title,'^MA_DESC:'+content,'^DDJ:'+author,'^REG_DATE:'+date,sep='\n')
except Exception as e:
    print(e)
    exit()