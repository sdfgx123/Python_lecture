from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome()
browser.get("http://naver.com")
elem=browser.find_element_by_class_name("link_login")
elem.click()
browser.back()
browser.forward()
browser.back()
elem=browser.find_element_by_id("query")
elem.send_keys("test")
elem.send_keys(Keys.ENTER)

while(True):
    pass