from selenium import webdriver
import requests
from bs4 import BeautifulSoup

browser=webdriver.Chrome("C:\chromedriver.exe")
browser.get("https://book.naver.com/bookdb/book_detail.nhn?bid=20875273")

while(True):
    pass
