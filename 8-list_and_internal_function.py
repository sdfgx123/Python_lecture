#리스트와 내장함수

import random as r

a = [] #빈 리스트 생성
print(a)

b = list() #빈 리스트 생성
print(b)

a = [1, 2, 3, 4, 5]
print(a)
print(a[0])

b = list(range(1, 11))
print(b)

c = a + b #리스트끼리 더해서 합치기 : a랑 b 리스트
print(c)

a.append(6) # a 리스트에 6 추가하기
print(a)

a.insert(3, 7) # a 리스트의 3번 인덱스에 7 삽입
print(a)

a.pop() # 마지막 인스턴스 제거
print(a)
a.pop(3) # 3번 인덱스의 인스턴스 제거
print(a)

a.remove(4) # 4라는 값을 찾아서 제거
print(a)

print(a.index(5)) # a 리스트에서 5라는 값을 가지는 인덱스 출력

# a 리스트 초기화 하고 다시 시작
a = list(range(1, 11))
print(a)
print(sum(a)) # 리스트의 모든 값 더하여 반환
print(max(a)) # 리스트에서 제일 큰 값 반환
print(min(a)) # 제일 작은 값 반환

r.shuffle(a) # a 리스트의 값들을 무작위로 섞음
print(a)
a.sort() # 오름차순 정렬
print(a)
a.sort(reverse=True) # 내림차순 정렬
print(a)
a.clear()
print(a) # 데이터 다 날림

# 8-2. 리스트와 내장함수 두번째 강의, 20210515
a = [23, 12, 36, 53, 19]
print(a[:3])
print(len(a)) # a 리스트의 길이 출력

for i in range(len(a)):
    print(a[i], end=' ') # a 리스트의 길이만큼 차례대로 출력하는데, 구분은 띄어서 해라
print()

for x in a: # 위 for문이랑 똑같은 결과
    print(x, end=' ')
print()

for x in a: # 홀수만 출력
   if x%2==1:
       print(x, end=' ')
print()

# a 리스트를 튜플 형태로 저장해서 출력
for x in enumerate(a): # enumerate : 튜플 형태로 데이터를 바꾸는 함수인 듯?
    print(x)

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

if all(50 > x for x in a): # all : 조건이 모두 참일 때
    print('YES')
else:
    print('NO')

if any(15 > x for x in a): # any : 하나라도 참인 게 있을 때
    print('YES')
else:
    print('NO')