import requests
from bs4 import BeautifulSoup

for i in range(1, 4):

    #url="https://www.yna.co.kr/industry/technology-science/"+str(i)
    url="https://www.hankyung.com/economy/0401?page="+str(i)
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")

    for j in range(15):

        test = soup.select('div.article a')[j]['href']
        url=test
        res=requests.get(url)
        res.raise_for_status()
        soup=BeautifulSoup(res.text, "lxml")

        title=soup.find('title').get_text()
        title=title[:-7]
        
        date=soup.find('meta', attrs={'property':'article:published_time'})
        date=str(date)
        date=date[15:]
        date=date[:-37]
        author=soup.find('meta', attrs={'property':'article:author'})['content']

        print("^[url:", test)
        #print("^[title:", title)
        #print("^[author:", author)
        #print("^[date:", date)
