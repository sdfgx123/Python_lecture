# 인접행렬 (가중치 방향그래프)
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_6\input.txt", "rt")
n, m=map(int, input().split())
g=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b, c=map(int, input().split())
    g[a][b]=c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()