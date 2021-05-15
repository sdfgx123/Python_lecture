# 람다 함수

'''
def plus_one(x):
    return x + 1

print(plus_one(1))
'''

# 람다 함수 호출
plus_two = lambda x: x+2 # plus_two는 변수명임
print(plus_two(1))

# 람다 실제로 쓰이는 경우
a = [1, 2, 3]
print(list(map(lambda x: x+1, a)))