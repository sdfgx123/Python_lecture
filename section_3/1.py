# Section 3 : 탐색 & 시뮬레이션 (String, 1차원, 2차원 리스트 탐색)
# 회문 문자열 검사

import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_3\input.txt", "rt")

n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

'''
다른 방법
print(s[::-1]): s 배열의 맨 끝자리부터 하나씩 앞으로 출력
    print("#%d YES" %(i+1)) 이렇게 해도 결과 똑같음

if s == s[::-1]:
    print("#%d YES" %(i+1))
else:
    print("#%d NO" %(i+1))
'''