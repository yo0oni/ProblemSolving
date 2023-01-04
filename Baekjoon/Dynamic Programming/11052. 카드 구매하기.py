n = int(input())
price = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], price[j] + dp[i-j])
        # dp[1] == p[1]
        # dp[2] == dp[1] + p[1], p[2] 
        # dp[3] == dp[1] + p[2], dp[2] + p[1], p[3]
        # dp[4] == dp[1] + p[3], dp[2] + p[2], dp[3] + p[1], p[4]
print(dp[n])