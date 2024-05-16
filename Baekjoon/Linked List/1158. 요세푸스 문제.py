import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = []
for i in range(1, n+1):
    numbers.append(i)

answer = []
index = 0

for t in range(n):
    index += k-1  

    if index >= len(numbers):
        index = index % len(numbers)
 
    answer.append(str(numbers.pop(index)))

print("<", ", ".join(answer),">", sep='')