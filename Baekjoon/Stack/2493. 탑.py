import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))
stack = []
answer = [0] * n


for i in range(n):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()

    if stack:
        answer[i] = stack[-1] + 1
    stack.append(i)

print(" ".join(map(str, answer)))