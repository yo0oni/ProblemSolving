import sys
input = sys.stdin.readline

n = int(input())
km = list(map(int, input().split()))
prices = list(map(int, input().split()))

answer = 0
answer += km[0] * prices[0]
min_price = prices[0]

for idx in range(len(km)-1):
    if min_price > prices[idx+1]:
        min_price = prices[idx+1]

    answer += min_price*km[idx+1]

print(answer)