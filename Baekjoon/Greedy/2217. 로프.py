import sys
input = sys.stdin.readline

n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)
max_weight = 0
for i in range(n, 0, -1):
    if rope[i-1] * i > max_weight:
        max_weight = rope[i-1] * i

print(max_weight)