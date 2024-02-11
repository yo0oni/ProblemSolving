import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    # 동전 종류 개수
    n = int(input())

    # 동전 종류
    coins = list(map(int, input().split()))

    # 원하는 금액
    m = int(input())

    ways = 0
    dp = [0 for _ in range(m+1)]
    dp[0] = 1

    for i in range(n):
        for j in range(coins[i], m+1):
            dp[j] += dp[j - coins[i]]
        
    print(dp[m])