import requests
from bs4 import BeautifulSoup

url="https://play.google.com/store/movies/top"
res=requests.get(url)
res.raise_for_status()
soup=BeautifulSoup(res.text, "lxml")

movies=soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

with open("movie.html", "w", encoding="utf-8") as f:
    #f.write(res.text)
    f.write(soup.prettify(  )) # html 문서 예쁘게 출력
