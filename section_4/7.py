# 창고정리(그리디)
import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_4\input.txt", "rt")
L=int(input())
list=list(map(int, input().split()))
m=int(input())
list.sort()
for _ in range(m):
    list[0]+=1
    list[L-1]-=1
    list.sort()
print(list[L-1]-list[0])