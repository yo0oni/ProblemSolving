import math

# 진수 변환
def change(n, k):
    string = ''
    while n > 0:
        n, remain = divmod(n, k)
        string += str(remain)
    return ''.join(reversed(string))
    
# 소수 판별
def isprime(n):
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
        
    return True
    
def solution(n, k):
    answer = 0
    change_k = change(n, k)
    
    p = change_k.split('0')
    p = [int(v) for v in p if v]
    
    for i in p:
        if isprime(i):
            answer += 1
    
    return answer