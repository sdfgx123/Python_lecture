# 사과나무(BFS)
import sys
from collections import deque
sys.stdin=open("C:\Python-lecture\Python_lecture\section_7\input.txt", "rt")

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
# ch : 방문 했는지 안했는지 체크하기 위해서, 2차원 배열
ch=[[0]*n for _ in range(n)]
sum=0
Q=deque()
# 중앙 지점에 방문했다고 체크 걸어줌
ch[n//2][n//2]=1
sum+=a[n//2][n//2]
Q.append((n//2, n//2))
# 레벨 0이다
L=0

while True:
    # L이 2로 나눈 몫에 다다르면 더 이상 진행하면 안됨
    if L==n//2:
        break
    size=len(Q)
    for i in range(size):
        tmp=Q.popleft()
        for j in range(4):
            x=tmp[0]+dx[j]
            y=tmp[1]+dy[j]
            if ch[x][y]==0:
                sum+=a[x][y]
                ch[x][y]=1
                Q.append((x, y))
    L+=1
print(sum)