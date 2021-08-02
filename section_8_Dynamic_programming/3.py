# 도전과제 계단오르기(top down 메모이제이션)
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_8_Dynamic_programming\input.txt", "rt")
n=int(input())
dy=[0]*(n+1)
dy[1]=1
dy[2]=2
for i in range(3, n+1):
    dy[i]=dy[i-1]+dy[i-2]
print(dy[n])