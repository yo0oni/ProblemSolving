import sys

n = int(input())
bar = [0 for _ in range(1001)]
answer = 0
max_h = 0

for _ in range(n):
    idx, height = map(int,sys.stdin.readline().split())
    bar[idx] = height
    if height > max_h:
        max_h = height
        max_idx = idx

max_h = 0
for i in range(max_idx+1): # 왼쪽 그룹
    max_h = max(max_h, bar[i])
    answer += max_h

max_h = 0
for i in range(1000, max_idx, -1): # 오른쪽 그룹
    max_h = max(max_h, bar[i])
    answer += max_h

print(answer)