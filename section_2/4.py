# 4. 대푯값

import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_2\input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
min = 2147000000
ave = round(sum(a) / n) # round : 소수 첫째 자리에서 반올림
for idx, x in enumerate(a): # enumerate : idx 인덱스값, x 변수값을 1:1 대응시켜 주는 역할
    tmp = abs(x-ave) # abs : 절댓값 반환
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)

'''
대푯값 round 함수 관련 이슈 : round는 round_half_even 방식을 택하기 때문에 4.5000 처럼 소수점이 정확히 절반일 경우 짝수 쪽으로 이동하게 됨
즉, 4.5000 -> 4, 5.5000 -> 6 으로 변환됨
'''