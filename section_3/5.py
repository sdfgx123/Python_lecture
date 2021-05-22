# 수의 합 / 이해 완벽하지는 않음, 더 봐야 함
import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_3\input.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)