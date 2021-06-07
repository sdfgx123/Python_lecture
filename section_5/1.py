# 가장 큰 수(스택)
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_5\input.txt", "rt")
num, m=map(int, input().split())
num=list(map(int, str(num)))
stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m] #슬라이싱 : 뒤에서 m번째 바로 앞에서 끊음
res=''.join(map(str, stack)) #조인 활용해서 출력, for문 돌려도 됨
print(res)

'''
for문 이용해서 stack 출력하는 방법
for x in stack:
    print(x, end='')
'''