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
