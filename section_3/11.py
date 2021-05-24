# 격자판 회문수
import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_3\input.txt", "rt")
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5] # 슬라이싱 : 예를 들어, i=0이면 i=0부터 i=4까지
        if tmp==tmp[::-1]: # 거꾸로 돌려서 같으면
            cnt+=1
        for k in range(2):
            if board[i+k][j]!=board[i+5-k-1][j]: # 예를 들어, 맨 처음과 맨 끝을 하나씩 비교해 나간다고 생각하면 됨
                break
        else:
            cnt+=1
print(cnt)