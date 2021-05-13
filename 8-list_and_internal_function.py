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