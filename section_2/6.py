# 자릿수의 합

import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_2\input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10 # 10으로 나눈 나머지
        x = x // 10 # 10으로 나눈 몫
    return sum

max = 0;

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)

# 이거는 string 처리해서 푸는 방법
'''
def digit_sum(x):
    sum = 0
    for i in str(x): # str() 함수를 통해 리스트의 숫자를 문자로 바꿔버림
        sum += int(i) # sum에는 string으로 바꾼 숫자의 각 자릿수들을 int로 바꿔서 sum에 더함
    return sum # sum 반환
'''