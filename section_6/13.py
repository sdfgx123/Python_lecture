# 경로 탐색(그래프 DFS)
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_6\input.txt", "rt")
def DFS(v):
    global cnt
    if v==n:
        cnt+=1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n+1):
            # v번째 노드에서 i번째 노드로 갈 수 있느냐?
            # ch[i] : 중복방문 안되기 때문에 방문하지 않았어야 함
            if g[v][i]==1 and ch[i]==0:
                ch[i]=1
                path.append(i)
                DFS(i)
                # pop 하는 이유 : 넣었던 거 빼줘야 하기 때문
                path.pop
                ch[i]=0


if __name__ == "__main__":
    n, m = map(int, input().split())
    # g : 그래프
    g = [[0] * (n+1) for _ in range(n+1)]
    ch = [0] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    path=[]
    path.append(1)
    ch[1] = 1
    DFS(1)
    print(cnt)