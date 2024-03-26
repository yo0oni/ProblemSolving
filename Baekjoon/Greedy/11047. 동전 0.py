import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
count = 0
for coin in coins:
    if coin <= k:
        count += (k // coin)
        k %= coin

print(count)