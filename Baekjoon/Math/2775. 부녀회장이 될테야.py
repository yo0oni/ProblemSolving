import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    zero_floor = [i for i in range(1, n+1)]
    
    for floor in range(k):
        for number in range(1, n):
            zero_floor[number] += zero_floor[number-1]
            
    print(zero_floor[-1])