#숫자만 추출

import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_3\input.txt", "rt")
res = 0
s = input()
for x in s:
    if x.isdecimal(): # isdecimal : boolean, 대상이 0 ~ 9의 숫자가 맞는지 아닌지 검사하여 반환
        res = res * 10 + int(x)
print(res)
cnt = 0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)