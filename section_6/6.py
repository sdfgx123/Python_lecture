# 중복순열 구하기
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_6\input.txt", "rt")
input=sys.stdin.readline

def DFS(L):
    global cnt
    if L==m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            res[L]=i
            DFS(L+1)

if __name__=="__main__":
    n, m=map(int, input().split())
    res=[0]*m
    cnt=0
    DFS(0)
    print(cnt)