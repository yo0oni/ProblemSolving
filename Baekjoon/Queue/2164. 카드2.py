import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
numbers = deque()
for i in range(1, n+1):
    numbers.append(i)

while len(numbers) > 1:
    numbers.popleft()
    top = numbers.popleft()
    numbers.append(top)

print(*numbers)