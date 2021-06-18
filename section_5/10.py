# 최소힙
import sys
import heapq as hq # 힙 큐를 임포트함
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
            print(hq.heappop(a)) # 루트 노드값 반환
    else:
        hq.heappush(a, n)
        