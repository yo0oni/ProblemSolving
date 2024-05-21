import sys
input = sys.stdin.readline

n = int(input())
heights = []
stack = []
total_count = 0

for _ in range(n):
    heights.append(int(input()))

for height in heights:

    while stack and stack[-1] <= height:
        stack.pop()

    total_count += len(stack)
    stack.append(height)

print(total_count)