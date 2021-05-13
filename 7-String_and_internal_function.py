# 문자열과 내장함수

msg = 'It is Time'


for x in msg:
    if x.isupper(): # msg 중에서 대문자가 있으면
        print(x, end=' ') # 그 대문자를 출력하고, 줄바꿈 하지 말고 띄어서 나열해라
print() # 줄 바꿔라

for x in msg:
    if x.islower(): # msg 중에서 소문자가 있으면
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha(): # x가 알파벳일 경우에만 참이 된다
        print(x, end='')
print()

tmp = 'AZ'

for x in tmp:
    print(ord(x)) # x의 아스키 넘버를 출력해라

tmp = 'az'

for x in tmp:
    print(ord(x)) # x의 아스키 넘버를 출력해라

tmp = 65
print(chr(tmp)) # 대응되는 숫자의 아스키 넘버에 해당하는 문자 출력