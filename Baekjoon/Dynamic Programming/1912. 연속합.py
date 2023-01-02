n = int(input())
l = list(map(int, input().split()))

dp = [0]*n
dp[0] = l[0]
# 연속된 합이 음수가 되기 전까지 계속 더하기
# 연속된 합이 음수가 된다는 것 -> 최대값이 나올 수 없음
for i in range(1, n): # 1 ~ 9
    if dp[i-1] > 0:
        dp[i] = dp[i-1] + l[i]
    
    else:
        dp[i] = l[i]

print(max(dp))