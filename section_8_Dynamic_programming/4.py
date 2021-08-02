# 도전과제 돌다리 건너기 bottom up
# 쉽게 생각해서, top down은 DFS, bottom up은 dynamic programming 생각
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_8_Dynamic_programming\input.txt", "rt")

# def DFS(x):
#     if dy[x]>0:
#         return dy[x]
#     if x==1 or x==2:
#         return x
#     else:
#         dy[x]=DFS(x-1)+DFS(x-2)
#         return dy[x]

# if __name__=="__main__":
#     n=int(input())
#     dy=[0]*(n+1)
#     print(DFS(n))

n=int(input())
dy=[0]*(n+1)
dy[1]=1
dy[2]=2
for i in range(3, n+1):
    dy[i]=dy[i-1]+dy[i-2]
print(dy[n])