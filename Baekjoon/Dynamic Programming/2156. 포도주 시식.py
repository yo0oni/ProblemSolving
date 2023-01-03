import sys

# n번째까지 마셨을 때 최대로 마실 수 있는 포도주의 양을 ​Dn
# 1번째 포도주까지 먹었을 때 최대로 마실 수 있는 포도주 양(D1)​은 W1​
# D2 == W1 + W2​

# D3​는 ​(W1+W2), (W1+W3)​, (W2+W3) 중 최대값
# D3를 다시 쓰면 max(D2, D1+W3, D0+W2+W3)
# 점화식을 사용했을 때 n번째까지 최대로 마실 수 있는 포도주의 양은
# max(Dn - 1, Dn-2 + Wn, Dn-3 + Wn-1 + Wn)

n = int(input())
w = []
dp = [0]*n

for _ in range(n):
    w.append(int(sys.stdin.readline().rstrip()))

dp[0] = w[0]

if n>1:
    dp[1] = w[0] + w[1]
if n>2:
    dp[2] = max(w[2]+w[1], w[2]+w[0], dp[1])
# w == [6, 10, 13, 9, 8, 1]
# dp == [6, 16, 23]

for i in range(3, n):
    # dp[3] = max(23, 26, 28) == 28
    # dp[4] = max(28, 31, 33) == 33
    # dp[5] = max(33, 29, 32) == 33
    dp[i] = max(dp[i-1], dp[i-2]+w[i], dp[i-3]+w[i-1]+w[i])

print(max(dp))