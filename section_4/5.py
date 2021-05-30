# 회의실 배정(그리디)
import sys
sys.stdin=open("C:\python_lecture\Python_lecture\section_4\input.txt", "rt")
n=int(input())
meeting=[]
for i in range(n):
    s, e=map(int, input().split())
    meeting.append((s, e)) #튜플 자료형으로 리스트에 추가
meeting.sort(key=lambda x : (x[1], x[0])) # e 우선하여 리스트를 정렬함. 이때 람다 함수를 사용함.
et=0 # end time : 회의가 끝나는 시간을 체크하기 위함
cnt=0
for s, e in meeting:
    if s>=et:
        et=e
        cnt+=1
print(cnt)