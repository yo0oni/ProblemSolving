import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list()

for i in range(0, n+1):
    numbers.append(i)

for _ in range(m):
    i, j = map(int, input().split())
    numbers = numbers[:i] + (numbers[i:j+1])[::-1] + numbers[j+1:]

print(*numbers[1:])