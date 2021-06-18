# 최대힙
import sys
import heapq as hq
sys.stdin=open("C:\Python-lecture\Python_lecture\section_5\input.txt", "rt")
a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a)) # 출력할 때 - 붙여서 원래 숫자로 변환
    else:
        hq.heappush(a, -n) # 최소 힙 코드를 활용함, 부호를 바꿔서 push함