# 점수계산

import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_2\input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

sum = 0
cnt = 0

for x in a:
    if x==1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)