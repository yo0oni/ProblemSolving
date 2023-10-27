import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
result = [-1] * n
stack = []

for index in range(n):
    while stack and numbers[stack[-1]] < numbers[index]:
        result[stack.pop()] = numbers[index]
    stack.append(index)
    
print(*result)