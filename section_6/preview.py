# 재귀함수와 스택 선수지식
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_6\input.txt", "rt")
def DFS(x):
    if x>0:
        DFS(x-1)
        print(x, end=' ')

if __name__=="__main__":
    n=int(input())
    DFS(n)