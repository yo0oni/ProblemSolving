import sys
input = sys.stdin.readline

# 3개를 사면 그 중 제일 싼게 무료
n = int(input())
prices = []
for _ in range(n):
    prices.append(int(input()))

prices.sort(reverse=True)
answer = 0
while len(prices) > 2:
    answer += sum(prices[:2])
    prices = prices[3:]

answer += sum(prices)
print(answer)