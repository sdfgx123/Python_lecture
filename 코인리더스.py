import requests
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from urllib import parse
import sys

coin_urls = []
f=open("코인리더스.txt", 'w', encoding="UTF-8")

# 200 : 정상
for i in range(1, 4):
    url = "https://www.coinreaders.com/sub.html?page=" + str(i) + "&section=sc10&section2="
    res=requests.get(url)
    # 만약 문제가 있다면 즉시 종료한다
    res.raise_for_status()
    #print("응답코드 :", res.status_code)

    # 가져온 html 문서를 lxml parser를 통해서 beautifulsoup 객체로 만듦
    soup=BeautifulSoup(res.content, "lxml")

    #print(soup.title.get_text())
    #print(soup.find('div dl dt a', {'class':'sub_read_list_box'}).get_text())

    #print(soup.select('div.sub_read_list_box > dl > dt')[0].text) # 기사 제목만 가져옴

    """ titles = soup.select('div.sub_read_list_box > dl > dt') # 기사 제목들 가져오기
    for title in titles:
        print(title.text) """

    #print(soup.select('div.sub_read_list_box > dl > dt > a')[0]['href']) # 기사 링크

    links = soup.select('div.sub_read_list_box > dl > dt > a')
    for link in links:
        #print(link['href'])
        coin_urls.append("https://www.coinreaders.com" + link['href'])
    #print(coin_urls)

for coin_url in (coin_urls):
    url = coin_url
    res=requests.get(url)
    soup=BeautifulSoup(res.content, "lxml")
    #print(soup.select('div.article_head > h1'))
    
    """ names = soup.select_one('div.article_head > h1')
    for name in names:
        print(name.text) """
    name = soup.select_one('div.article_head > h1')
    author = soup.find('meta', {'property':'dable:author'}).get('content')
    date = soup.find('meta', {'property':'article:published_time'}).get('content')
    content = soup.select_one('#textinput > p')
    f.write('^MA_TITLE:'+ name.text + '\n')
    f.write('^DDJ:' + author + '\n')
    f.write('^REG_DATE:' + date + '\n')
    f.write('^MA_DESC:' + content.text + '\n')
    
print('done')
    
    #title = soup.select('div.article_head > h1')
    #print(title.text)
    #title = crObject.find('meta', {'property':'og:title'}).get('content')