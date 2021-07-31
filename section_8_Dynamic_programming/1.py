# 동적계획법, 네트워크 선 자르기, Bottom-Up
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_8_Dynamic_programming\input.txt", "rt")
n=int(input())
# 인덱스 0번 버리고 1번부터 사용하려고
dy=[0]*(n+1)
# 직관적으로 알 수 있는 것들은 직접 초기화
dy[1]=1
dy[2]=2
for i in range(3, n+1):
    dy[i]=dy[i-1]+dy[i-2]
print(dy[n])