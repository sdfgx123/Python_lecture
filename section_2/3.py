# k번째 큰 수

import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_2\input.txt", "rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))

res = set() # set 자료구조 : 중복 제거
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i] + a[j] + a[m]) # 중복을 제거하며 set 자료구조에 저장
res = list(res) # set 자료구조는 정렬할 수 없기 때문에 list화 해야 함
res.sort(reverse=True) # 내림차순 정렬
print(res[k-1]) # k가 아니라 k-1인 이유 : 인덱스 구조는 1이 아니라 0부터 시작하기 때문