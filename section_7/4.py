# 동전 바꿔주기(DFS)
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_7\input.txt", "rt")
def DFS(L, sum):
    global cnt
    if sum>T:
        return
    if L==k:
        if sum==T:
            cnt+=1
    else:
        for i in range(cn[L]+1):
            DFS(L+1, sum+(cv[L]*i))

if __name__=="__main__":
    T=int(input())
    k=int(input())
    cv=list()
    cn=list()
    for i in range(k):
        a, b=map(int, input().split())
        cv.append(a)
        cn.append(b)
    cnt=0
    DFS(0, 0)
    print(cnt)