import requests
from bs4 import BeautifulSoup

#f=open("210914_3.txt", 'w')

for i in range(1, 4):
    url="https://www.mk.co.kr/news/stock/?page="+str(i)
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")

    for j in range(10):
        test = soup.select('dd.thumb a')[j]['href']
        url=test
        res=requests.get(url)
        res.raise_for_status()
        soup=BeautifulSoup(res.text, "lxml")

        title=soup.find('h1', attrs={'class':'top_title'}).get_text()
        print(title)
        """ title=title[:-7]
        date=soup.find('meta', attrs={'property':'article:published_time'})['content']
        author=soup.find('meta', attrs={'property':'article:author'})['content'] """

        """ print("^[url:", test)
        print("^[title:", title)
        print("^[author:", author)
        print("^[date:", date)
        test="^[url:"+test+'\n'
        title="^[title:"+title+'\n'
        author="^[author:"+author+'\n'
        date="^[date:"+date+'\n'
        f.write(test)
        f.write(title)
        f.write(author)
        f.write(date) """
