import sys
input = sys.stdin.readline

n, k = map(int, input().split())
heights = list(map(int, input().split()))
diff = [0] * (n-1)

for idx in range(n-1):
    diff[idx] = heights[idx+1] - heights[idx]

diff.sort(reverse=True)
print(sum(diff[k-1:]))