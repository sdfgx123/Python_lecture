# 2차원 리스트 생성과 접근

'''
a = [0] * 3
print(a)
'''

a = [[0]*3 for _ in range(3)] # 언더바 하면 변수 없이 반복문만 도는 것임
print(a)

a[1][1]  = 2
print(a)

for x in a:
    print(x)

for x in a:
    for y in x:
        print(y, end=' ')
    print()