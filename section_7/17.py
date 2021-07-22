# 피자 배달 거리(삼성 SW 역량평가 기출문제 : DFS 활용)
import sys
from collections import deque
sys.stdin=open("C:\Python-lecture\Python_lecture\section_7\input.txt", "rt")

def DFS(L, s):
    global res
    if L==m:
        sum=0
        for j in range(len(hs)):
            # 집의 좌표
            x1=hs[j][0]
            y1=hs[j][1]
            dis=2147000000
            for x in cb:
                # 피자집의 좌표
                x2=pz[x][0]
                y2=pz[x][1]
                # 절댓값 비교하여 dis 결정
                dis=min(dis, abs(x1-x2)+abs(y1-y2))
            sum+=dis
        if sum<res:
            res=sum
    else:
        for i in range(s, len(pz)):
            cb[L]=i
            DFS(L+1, i+1)

if __name__=="__main__":
    n, m=map(int, input().split())
    board=[list(map(int, input().split())) for _ in range(n)]
    # 집의 좌표 정보
    hs=[]
    # 피자집의 좌표 정보
    pz=[]
    # 조합의 경우의 수가 저장될 리스트
    cb=[0]*m
    res=2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                hs.append((i, j))
            elif board[i][j]==2:
                pz.append((i, j))
    DFS(0, 0)
    print(res)