from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("https://book.naver.com/bookdb/book_detail.nhn?bid=20884852")
bsObject=BeautifulSoup(html, "html.parser")


for meta in bsObject.body.find_all('div', {"class":"dsc"}):
    print(meta.get('p'))
