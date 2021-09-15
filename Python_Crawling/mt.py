import requests
from bs4 import BeautifulSoup

for i in range(1, 4):

    url="https://news.mt.co.kr/newsList.html?type=1&comd=&pDepth=news&pDepth1=tech&pDepth2=Ttotal&page="+str(i)
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, 'lxml')


    for j in range(15):

        tmp=soup.select('strong.subject a')[j]['href']
        url='\"'+tmp+'\"'
        print(url)

        title=soup.find('title').get_text()
        print(title)

        #res=requests.get(url)
        #res.raise_for_status()
        #soup=BeautifulSoup(res.text, 'lxml')

        #title=soup.find('title').get_text()
        #print(title)
if __name__=="__main__":
    
    for i in range(1, 4):

        url="https://news.mt.co.kr/newsList.html?type=1&comd=&pDepth=news&pDepth1=tech&pDepth2=Ttotal&page="+str(i)
        res=requests.get(url)
        res.raise_for_status()
        soup=BeautifulSoup(res.text, 'lxml')
        