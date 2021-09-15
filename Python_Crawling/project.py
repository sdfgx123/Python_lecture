import requests
from bs4 import BeautifulSoup

url = "https://www.segye.com/newsList/0101030900000?page=1"

response = requests.get(url)

if response.status_code == 200:
    print(response)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('div#wapCont>div#wps_layout1>section#contMain>div#wps_layout1_box1>ul.listBox')
    # title_link = title.find('a')["href"]
    print(title)
else : 
    print(response.status_code)