import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_2\input.txt", "rt")
n, k = map(int, input().split())
cnt = 0

for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)