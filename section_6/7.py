# 동전교환
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_6\input.txt", "rt")
def DFS(L, sum):
    global res
    # res 보다 더 큰 레벨은 애초에 답이 아니므로 볼 팔요가 없다
    if L>res:
        return
    # sum이 거스름돈 보다 커져 버리면 종료시킨다
    if sum>m:
        return
    if sum==m:
        if L<res:
            res=L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])

if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    # m : 거스름돈
    m=int(input())
    res=2147000000
    a.sort(reverse=True)
    DFS(0, 0)
    print(res)