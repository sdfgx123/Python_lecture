# 양팔저울(DFS)
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_7\input.txt", "rt")
# L : 추가 G에 접근하는 인덱스
def DFS(L, sum):
    global res
    if L==n:
        if 0<sum<=s:
            res.add(sum)
    else:
        # 추를 왼쪽에 놓는다
        DFS(L+1, sum+G[L])
        # 추를 오른쪽에 놓는다
        DFS(L+1, sum-G[L])
        # L번째 추를 무게를 재는 데 사용하지 않겠다
        DFS(L+1, sum)

if __name__=="__main__":
    n=int(input())
    G=list(map(int, input().split()))
    # s : 추 무게의 총합, res : set 자료구조 / 중복 제거

    s=sum(G)
    res=set()
    DFS(0, 0)
    print(s-len(res))