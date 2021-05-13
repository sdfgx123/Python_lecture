#중첩 반복문, 2중 for문

for i in range(5):
    print('i:', i, sep='', end=' ')
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print()

#5X5 별찍기
for i in range(5):
    for j in range(5):
        print("*", end=' ') #end : 줄바꿈 안하고 한 칸 띄어서 구분
    print() #줄바꿈

#직각삼각형 별찍기
for i in range(5):
    for j in range(i+1):
        print("*", end=' ')
    print()

#직각삼각형 반대로
for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()