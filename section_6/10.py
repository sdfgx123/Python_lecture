# 조합 구하기(DFS)
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_6\input.txt", "rt")
def DFS(L, s):
    global cnt
    if L==m:
        for j in range(L):
            print(res[j], end=' ')
        cnt+=1
        print()
    else:
        for  i in range(s, n+1):
            res[L]=i
            DFS(L+1, i+1)

if __name__=="__main__":
    n, m=map(int, input().split())
    res=[0]*(n+1)
    cnt=0
    DFS(0, 1)
    print(cnt)