# 사다리 타기(DFS)
import sys
from collections import deque
sys.stdin=open("C:\Python-lecture\Python_lecture\section_7\input.txt", "rt")
def DFS(x, y):
    ch[x][y]=1
    # 사다리 끝에 도달했으면 y를 출력한다
    if x==0:
        print(y)
    else:
        # 사다리 왼쪽 탐색하는 경우
        if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x, y-1)
        # 사다리 오른쪽으로 이동하는 경우
        elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x, y+1)
        # 왼쪽도, 오른쪽도 아님, 행 번호만 감소시킴, 즉 위로 올라간다
        else:
            DFS(x-1, y)

if __name__=="__main__":
    board=[list(map(int, input().split())) for _ in range(10)]
    ch=[[0]*10 for _ in range(10)]
    for y in range(10):
        if board[9][y]==2:
            DFS(9, y)