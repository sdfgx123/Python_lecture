# 소수(에라토스테네스의 체)

import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_2\input.txt", "rt")

n = int(input())
ch = [0]*(n+1) # 소수 소거하는 스위치 같은 개념
cnt = 0

for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i): # i부터 시작, n+1까지 반복, i씩 증가, 왜냐하면 i의 배수들을 소수에서 소거해야 하기 때문
            ch[j]=1
print(cnt)