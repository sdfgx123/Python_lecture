# 교육과정 설계
import sys
from collections import deque
sys.stdin=open("C:\Python-lecture\Python_lecture\section_5\input.txt", "rt")
need=input()
n=int(input())
for i in range(n):
    plan=input()
    dq=deque(need)
    for x in plan:
        if x in dq:
            if x!=dq.popleft():
                print("#%d NO" %(i+1))
                break
    else: # dq 순서대로 제대로 넘어왔다면, 즉 break 안 먹고 왔다면
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))