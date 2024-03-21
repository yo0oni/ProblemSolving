import sys
input = sys.stdin.readline

numbers = []
for _ in range(10):
    numbers.append(int(input()) % 42)

print(len(set(numbers)))