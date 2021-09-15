from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib import parse
import sys

#f=open("210914_10.txt", 'w')

for i in range(2, 5):
    url = "https://book.naver.com/bestsell/bestseller_list.nhn?cp=conects&cate=103&bestWeek=2021-09-2&indexCount="+str(i)+"&type=list"

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(30) #브라우저에서 사용되는 엔진 자체에서 파싱되는 시간을 기다려주는 메소드

    # 네이버의 베스트셀러 웹페이지를 가져온다.
    driver.get(url)
    crObject = BeautifulSoup(driver.page_source, 'html.parser')

    # 책의 상세 웹페이지 주소를 추출하여 리스트에 저장한다.
    book_page_urls = []
    for index in range(0, 10): #상세페이지 방문 횟수
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
        text = crObject.find('meta', {'property':'og:description'}).get('content')
        #text = crObject.find(id="bookIntroContent").get_text()
        #print(text)

        """ f.write("^[MA_TITLE:"+title+"\n")
        f.write("^[DDJ:"+author+"\n")
        f.write("^[REG_DATE:"+date+"\n")
        f.write("^[MA_DESC:"+text+"\n") """

        print('^MA_TITLE:'+title,'^MA_DESC:'+text+'\n','^DDJ:'+author,'^REG_DATE:'+date,sep='\n')
