# k번째 수

import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_2\input.txt", "rt")

T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a  = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))