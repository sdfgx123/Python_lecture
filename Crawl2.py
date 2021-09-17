import requests
from bs4 import BeautifulSoup
import sys

# 200 : 정상
res=requests.get("https://www.coinreaders.com/sub.html?page=1&section=sc10&section2=")
# 만약 문제가 있다면 즉시 종료한다
res.raise_for_status()
print("응답코드 :", res.status_code)