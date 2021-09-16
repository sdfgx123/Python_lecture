import requests
from bs4 import BeautifulSoup
#f=open("210914_4.txt", 'w')
for i in range(1, 4):
    url="https://www.yna.co.kr/industry/technology-science/"+str(i)
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")
    #title=soup.find('ul', attrs={'class':'listBox'})
    #title=soup.select_one('#wps_layout1_box1 > ul > li:nth-child(1) > a')
    #print(soup.title)
    #print(soup.title.get_text())
    #print(soup.a['href'])
    #print(soup.find_all(attrs={'class':'listBox'}))
    for j in range(25):
        test = soup.select('div.news-con a')[j]['href']
        test="https://"+test[2:]
        url=test
        res=requests.get(url)
        res.raise_for_status()
        soup=BeautifulSoup(res.text, "lxml")
        title=soup.find('title').get_text()
        title=title[:-7]
        #date=soup.select('meta',)
        date=soup.find('meta', attrs={'property':'article:published_time'})['content']
        #date=str(date)
        #date=date[15:]
        #date=date[:-37]
        author=soup.find('meta', attrs={'property':'article:author'})['content']
        #text=soup.find('div', {'class':'comp-box photo-group'}).find_next_siblings('p')[0].text.strip()
        #author=soup.select('strong.tit-name')
        #author=soup.find('meta', attrs={"class":"tit-name"}).get_text()

        #test=soup.find_all("a", attrs={"class":"tit-wrap"})[0]['href']
        #test2=soup.a['href'].get_text()
        print("^[url:", test)
        print("^[title:", title)
        #print("^[text:", text)
        print("^[author:", author)
        print("^[date:", date)
        test="^[url:"+test+'\n'
        title="^[title:"+title+'\n'
        author="^[author:"+author+'\n'
        date="^[date:"+date+'\n'
        """ f.write(test)
        f.write(title)
        f.write(author)
        f.write(date) """
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
