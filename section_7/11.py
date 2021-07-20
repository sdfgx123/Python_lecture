# 등산경로(DFS)
import sys
from collections import deque
sys.stdin=open("C:\Python-lecture\Python_lecture\section_7\input.txt", "rt")

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for k in range(4):
            xx=x+dx[k]
            yy=y+dy[k]
            # board 조건 : 더 큰 쪽으로만 움직이기 때문
            if 0<=xx<n and 0<=yy<n and board[xx][yy]>board[x][y]:
                ch[xx][yy]=1
                DFS(xx, yy)
                ch[xx][yy]=0

if __name__=="__main__":
    n=int(input())
    board=[[0]*n for _ in range(n)]
    ch=[[0]*n for _ in range(n)]
    max=-2147000000
    min=2147000000
    for i in range(n):
        tmp=list(map(int, input().split()))
        for j in range(n):
            if tmp[j]<min:
                min=tmp[j]
                # sx, sy : start 지점의 좌표 지정하는 과정
                sx=i
                sy=j
            if tmp[j]>max:
                max=tmp[j]
                # 도착지점의 행렬 번호
                ex=i
                ey=j
            board[i][j]=tmp[j]
    ch[sx][sy]=1
    cnt=0
    DFS(sx, sy)
    print(cnt)
