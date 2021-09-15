from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

for i in range(1,11):
    url = 'http://tvdaily.asiae.co.kr/section.html?section=2&page=%d' % i
    html = urllib.request.urlopen(url)
    soupHtml = BeautifulSoup(html, 'html.parser')
    for a in soupHtml.find_all('a', href=True,attrs={'class':'secttl'}):
        print("Found the URL:", a['href'])
        