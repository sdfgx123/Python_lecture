
 #반복문을 이용한 문제풀이
 #1. 1부터 n까지 홀수 출력하기
 #2. 1부터 n까지의 합 구하기
 #3. n의 약수 출력하기


# 1번
'''
n = int(input())

for i in range(1, n+1):
    if i%2==1:
        print(i)
'''

#2번
'''
n = int(input())

sum = 0
for i in range(1, n+1):
    sum = sum + i
print(sum)
'''

#3번
n = int(input())
for i in range(1, n+1):
    if n%i == 0:
        print(i, end=' ')