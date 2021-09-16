from selenium import webdriver
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

url="https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
res=requests.get(url)
res.raise_for_status()
soup=BeautifulSoup(res.text, "lxml")
news_list=soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)
print(news_list)

#for test in tests:
#   print(test.get_text())