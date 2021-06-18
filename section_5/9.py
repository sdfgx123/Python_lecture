# 아나그램(딕셔너리 해쉬)
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_5\input.txt", "rt")
a=input()
b=input()
str1=dict()
str2=dict()
# for x in a:
#     str1[x]=str1.get(x, 0)+1
# for x in b:
#     str2[x]=str2.get(x, 0)+1

# for i in str1.keys():
#     if i in str2.keys():
#         if str1[i]!=str2[i]:
#             print("NO")
#             break
#     else:
#         print("NO")
#         break
# else:
#     print("YES")

# 추가 강의 : 아나그램 딕셔너리 개선코드
sH=dict()
for x in a:
    sH[x]=sH.get(x, 0)+1

for x in b:
    sH[x]=sH.get(x, 0)-1

for x in a:
    if sH.get(x)>0:
        print("NO")
        break
else:
    print("YES")

# 추가 강의 : C++ 풀듯이 풀어 본다고 함, 아스키 넘버 이용해서
str1=[0]*52
str2=[0]*52
for x in a:
    if x.isupper():
        # ord 함수 : 문자를 아스키 넘버로 변환해줌
        str1[ord(x)-65]+=1 # 대문자 이므로 65를 빼준다
    else:
        str1[ord(x)-71]+=1
for x in a:
    if x.isupper():
        # ord 함수 : 문자를 아스키 넘버로 변환해줌
        str2[ord(x)-65]+=1 # 대문자 이므로 65를 빼준다
    else:
        str2[ord(x)-71]+=1
for i in range(52):
    if str1[i]!=str2[i]:
        print("NO")
        break
else:
    print("YES")
