# 정다면체

import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_2\input.txt", "rt")

n, m = map(int, input().split())
cnt = [0]*(n+m+3) # cnt 리스트를 만드는데, 인스턴스는 전부 0이고, 길이는 n + m + 3임
max = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]
for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end = ' ')