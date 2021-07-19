# 휴가(삼성 SW역량평가 기출문제 : DFS활용)
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_7\input.txt", "rt")
def DFS(L, sum):
    # L이 날짜
    global res
    if sum>res:
        res=sum
    else:
        if L+T[L]<=n+1:
            DFS(L+T[L], sum+P[L])
        DFS(L+1, sum)

if __name__=="__main__":
    n=int(input())
    T=list()
    P=list()
    for i in range(n):
        a, b=map(int, input().split())
        T.append(a)
        P.append(b)
    res=-2147000000
    # insert 하는 아유 : 0번 인덱스를 0으로 초기화 하기 위해서
    T.insert(0, 0)
    P.insert(0, 0)
    DFS(1, 0)
    print(res)