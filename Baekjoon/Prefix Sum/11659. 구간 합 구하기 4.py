import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
sum = 0

for idx in range(n):
    sum += numbers[idx]
    prefix_sum.append(sum)

for _ in range(m):
  a, b = map(int, input().split())
  print(prefix_sum[b] - prefix_sum[a-1])