def solution(n):
    sum = 0
    for x in range(1,n+1):
        if x%2 == 0:
            sum += x
    return sum

#def solution(n):
#    answer = 0
#    for i in range(2, n+1, 2):
#        answer += i
#    return answer