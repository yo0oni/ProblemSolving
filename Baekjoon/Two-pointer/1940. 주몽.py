import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

start = 0
end = N - 1
count = 0

numbers = sorted(map(int, input().split()))

while start < end:
    sum = numbers[start] + numbers[end]

    if sum < M:
        start += 1

    elif sum > M:
        end -= 1

    else:
        count += 1
        start += 1
        end -= 1

print(count)