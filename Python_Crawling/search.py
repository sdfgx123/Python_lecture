import requests
from bs4 import BeautifulSoup

for i in range(1, 4):
    url="https://www.hani.co.kr/arti/science/technology/list"+str(i)+".html"
    result=requests.get(url)
    #result.raise_for_status()
    soup=BeautifulSoup(result.text, "lxml")

    for j in range(10):
        test = soup.select('h4.article-title a')[j]['href']
        print("https://www.hani.co.kr"+test)
        url="https://www.hani.co.kr/"+test
        result=requests.get(url)
        #result.raise_for_status()
        soup=BeautifulSoup(result.text, "lxml")
        """ title=soup.find('title').get_text()
        title=title[:-24]
        date=soup.find('meta', attrs={'property':'article:published_time'})['content']
        author=soup.find('meta', attrs={'property':'dd:author'})['content']
        print("^[url:", test)
        print("^[title:", title)
        print("^[author:", author)
        print("^[date:", date) """
