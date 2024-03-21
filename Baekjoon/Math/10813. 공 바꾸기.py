import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = []

for i in range(0, n+1):
    numbers.append(i)

for _ in range(m):
    a, b = map(int, input().split())
    temp = numbers[a]
    numbers[a] = numbers[b]
    numbers[b] = temp

print(*numbers[1:])