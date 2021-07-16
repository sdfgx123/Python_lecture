# 수열 추측하기
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_6\input.txt", "rt")
def DFS(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0


if __name__=="__main__":
    n, f = map(int, input().split())
    # p : 순열 
    # 리스트
    p = [0] * n
    # b : 이항계수 초기화 리스트
    b = [1] * n
    # ch : 중복 방지를 위한 체크
    ch = [0] * (n+1)
    # 조합 공식 응용 어떻게 한 것 같은데, 이해 잘 안됨
    for i in range(1, n):
        b[i] = b[i-1] * (n-i) // i
    DFS(0, 0)