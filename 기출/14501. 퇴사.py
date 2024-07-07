import sys
input = sys.stdin.readline

n = int(input())
schedules = []
for _ in range(n):
    time, money = map(int, input().split())
    schedules.append([time, money])

dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if i + schedules[i][0] > n:
        dp[i] = dp[i+1]
    
    else:
        dp[i] = max(dp[i+1], schedules[i][1] + dp[i+schedules[i][0]])
    
print(dp[0])