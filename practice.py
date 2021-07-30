def solution(n):
    global sum
    for i in range(1, n+1):
        if n%i==0:
            sum+=i
    answer=sum
    return answer

n=int(input())
sum=0
sum=solution(n)
print(sum)