from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib import parse
import sys

f = open("210914_.txt", 'w')

for i in range(1, 2):
    url = "https://www.yna.co.kr/industry/technology-science/"+str(i)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(30)

    driver.get(url)
    crObject = BeautifulSoup(driver.page_source, 'html.parser')

    news_urls = []

    """ for index in range(0, 10):
        dl_data = crObject.find('div', {'class':"news-con"})
        link = "https:"+dl_data.select('a')[0].get('href')
        news_urls.append(link)
        print(link) """
    
    #dl_data = crObject.find_all('div', attrs={'class':'news-con'})
    for index in range(10):
        dl_data = crObject.find('div', {'class':'news-con'})
        link = "https:" + dl_data.select('a')[0].get('href')
        news_urls.append(link)
    
    for news_url in (news_urls):

        driver.get(news_url)
        crObject = BeautifulSoup(driver.page_source, 'html.parser')

        title = crObject.find('meta', {'property':'og:title'}).get('content')
        print(title)
