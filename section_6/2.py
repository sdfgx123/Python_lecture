# 이진트리 순회 (깊이우선탐색)
# 전위순회 : 부왼오, 중위순회 : 왼부오, 후위순회 : 왼오부
import sys
sys.stdin=open("C:\Python-lecture\Python_lecture\section_6\input.txt", "rt")
def DFS(v):
    if v>7:
        return
    else:
        # 전위순회
        # print(v, end=" ")
        # DFS(v*2)
        # DFS(v*2+1)

        # 중위순회
        # DFS(v*2)
        # print(v, end=" ")
        # DFS(v*2+1)

        # 후위순회, 예시 : 병합정렬
        DFS(v*2)
        DFS(v*2+1)
        print(v, end=" ")

if __name__=="__main__":
    DFS(1)