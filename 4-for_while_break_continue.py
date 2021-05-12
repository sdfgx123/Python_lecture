'''
a = range(1, 11)
print(list(a))

for i in range(10):
    print("i")

i = 10
while i>=1:
    print(i)
    i=i-1


i=1
while True:
    print(i)
    if i==10:
        break
    i+=1
'''
# 비정상 종료가 아니라 정상적으로 종료된 후에 실행하는 것 : else, for문에서
for i in range(1, 11):
    print(i)
    if i>15:
        break
else:
    print(11)