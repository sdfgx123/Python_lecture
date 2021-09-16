import requests
from bs4 import BeautifulSoup

for i in range(1, 4):
    url="https://www.coinreaders.com/sub.html?page="+str(i)+"&section=sc2&section2="
    #print("url : "+url)
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")
    #title=soup.find('ul', attrs={'class':'listBox'})
    #title=soup.select_one('#wps_layout1_box1 > ul > li:nth-child(1) > a')
    #print(soup.title)
    #print(soup.title.get_text())
    #print(soup.a['href'])
    #print(soup.find_all(attrs={'class':'listBox'}))
    for j in range(10):
        tmp=soup.select('div.sub_read_list_box>dl>dt>a')[j]['href']
        #print("tmp : "+tmp)
        #test = soup.select('div.news-con a')[j]['href']
        #test="https://"+test[2:]
        tmp="https://coinreaders.com"+tmp
        url=tmp
        #print("기사 상세 페이지 url : " + url)
        res=requests.get(url)
        res.raise_for_status()
        soup=BeautifulSoup(res.text, "lxml")
        title=soup.find('title').get_text()[:-6]
        date=soup.find('meta', attrs={'property':'article:published_time'})
        date=str(date)
        date=date[15:]
        date=date[:-37]
        #title=soup.find('title').get_text()
        #title=title[:-7]
        #date=soup.select('meta',)
        #date=soup.find('meta', attrs={'property':'article:published_time'})
        #date=str(date)
        #date=date[15:]
        #date=date[:-37]
        #author=soup.select('strong.tit-name')
        #author=soup.find('meta', attrs={"class":"tit-name"}).get_text()

    #test=soup.find_all("a", attrs={"class":"tit-wrap"})[0]['href']
    #test2=soup.a['href'].get_text()
        #print("^[url:", test)
        print("^[url:", url)
        print("^[title:", title)
        print("^[date:", date)
        #print("^[date:", date)
        #print(author)
    #str(test)

    #f=open("210913_4.txt", 'w')
    #f.write(test)
    #f.close()


#url="https://www.segye.com/newsList/0101030900000?page=1"
#res=requests.get(url)
#res.raise_for_status()
#soup=BeautifulSoup(res.text, "lxml")


#title=soup.find("meta", attrs={"property":"me2:post_tag"})
#content=soup.find("div", attrs={"id":"bookIntroContent"})
#print("^[title:", title["content"])
#print("^[content:", content.p.get_text())
