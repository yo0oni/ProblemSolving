import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
count = 0

for _ in range(n):
    coin.append(int(input()))

coin.reverse()

for index in range(n):
    if k - coin[index] >= 0:
        count += k // coin[index]
        k = k % coin[index]
    
    if k == 0:
        break

print(count)