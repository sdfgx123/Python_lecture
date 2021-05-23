# 곳감(모래시계)
import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_3\input.txt", "rt")

n = int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0)) # 맨 앞에 있는 변수 날리고, 그 변수를 다시 append 해서 끝에 추가
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())
res=0
s=0
e=n-1
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)