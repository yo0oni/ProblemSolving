import sys
input = sys.stdin.readline

N = int(input())
start = end = 0
count = 0
sum = 0

while end <= N:
    if sum < N:
        end += 1
        sum += end

    elif sum > N:
        sum -= start
        start += 1

    else:
        count += 1
        end += 1
        sum += end

print(count)