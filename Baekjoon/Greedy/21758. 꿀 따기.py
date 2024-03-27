import sys
input = sys.stdin.readline

n = int(input())
honey = list(map(int, input().split()))
p_sum = [honey[0]] + [0] * (n - 1)
ans = 0	

for i in range(1, n):
    p_sum[i] = p_sum[i - 1] + honey[i]

for i in range(1, n - 1):
    right = 2 * p_sum[-1] - honey[0] - honey[i] - p_sum[i]
    left = p_sum[-1] - honey[-1] - honey[i] + p_sum[i - 1]
    mid = p_sum[i] - honey[0] + p_sum[-1] - p_sum[i - 1] - honey[-1]
    ans = max(ans, right, left, mid)

print(ans)