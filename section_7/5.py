# 동전 분배하기(DFS)
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_7\input.txt", "rt")
def DFS(L):
    global res
    if L==n:
        cha=max(money)-min(money)
        if cha<res:
            tmp=set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res=cha
    else:
        for i in range(3):
            money[i]+=coin[L]
            DFS(L+1)
            money[i]-=coin[L]
if __name__=="__main__":
    n=int(input())
    coin=[]
    money=[0]*3
    res=2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)