# 미로의 최단거리 통로(BFS 활용)
import sys
from collections import deque
sys.stdin=open("C:\Python-lecture\Python_lecture\section_7\input.txt", "rt")

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
board=[list(map(int, input().split())) for _ in range(7)]
dis=[[0]*7 for _ in range(7)]
Q=deque()
Q.append((0, 0))
# 한 번 방문한 곳은 1로 바꿈, 즉 벽으로 만들어 버린다
board[0][0]=1

while Q:
    tmp=Q.popleft()
    for i in range(4):
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:
            board[x][y]=1
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x, y))
if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])