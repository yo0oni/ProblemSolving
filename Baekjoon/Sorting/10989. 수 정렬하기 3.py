import sys
input = sys.stdin.readline

N = int(input())

numbers = [0] * 10001
for index in range(N):
    numbers[int(input())] += 1

for index in range(10001):
    if numbers[index] != 0:
        for _ in range(numbers[index]):
            print(index)