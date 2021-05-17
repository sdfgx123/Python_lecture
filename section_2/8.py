# 뒤집은 소수
import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_2\input.txt", "rt")
def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2 + 1): # 예를 들어, 1*16일 경우, 2*8처럼 절반까지만 돈다 이런 느낌, 즉 1과 자기 자신을 빼고 약수는 절반까지만 존재함
        if x % i == 0:
            return False
    else:
        return True

n = int(input())
a = list(map(int, input().split()))

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
