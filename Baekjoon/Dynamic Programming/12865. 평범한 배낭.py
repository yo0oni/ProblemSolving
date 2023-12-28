import sys
input = sys.stdin.readline
 
N, K = map(int,input().split())
dp = [0] * (K+1)

for _ in range(N):
    W, V = [int(x) for x in input().split()]
    if W > K:
        continue

    for j in range(K, 0, -1):
        if W + j <= K and dp[j] != 0:
            dp[j+W] = max(dp[j+W], dp[j] + V)

    dp[W] = max(dp[W], V)

print(max(dp))