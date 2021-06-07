# 쇠막대기(스택)
import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_5\input.txt", "rt")
s=input()
stack=[]
cnt=0
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        if s[i-1]=='(': # 레이저다
            stack.pop()
            cnt+=len(stack)
        else: # 쇠막대기의 끝
            stack.pop()
            cnt+=1
print(cnt)