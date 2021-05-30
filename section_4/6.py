#씨름선수(그리디)
import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_4\input.txt", "rt")
n=int(input())
list=[]
for i in range(n):
    height, weight=map(int, input().split())
    list.append((height, weight))
list.sort(reverse=True)
largest=0
cnt=0
for x, y in list:
    if y>largest:
        largest=y
        cnt+=1
print(cnt)