#증가수열 만들기(그리디)
import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_4\input.txt", "rt")
n=int(input())
a=list(map(int, input().split()))
lt=0
rt=n-1
last=0
res=""
tmp=[]
while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt], 'L'))
    if a[rt]>last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        res=res+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()
print(len(res))
print(res)