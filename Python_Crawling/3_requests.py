import requests
from bs4 import BeautifulSoup
import sys

# 200 : 정상
res=requests.get("https://google.com")
# 만약 문제가 있다면 즉시 종료한다
res.raise_for_status()
print("응답코드 :", res.status_code)

# 글자 수를 반환
print(len(res.text))

# mygoogle.html 이름으로 파일 생성
with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)