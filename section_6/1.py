# 재귀함수를 이용한 이진수 출력
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_6\input.txt", "rt")
def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2, end=' ')

if __name__=="__main__":
    n=int(input())
    DFS(n)