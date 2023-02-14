import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

x = list(map(int, input().split()))
min_height = 0
height = 0

if len(x) == 1:
    min_height = max(x[0] - 0, N - x[0])

for i in range(len(x)):
    if i == 0:
        height = x[i] - 0
    elif i == len(x) - 1:
        height = N - x[i]
    else:
        if (x[i] - x[i-1])%2:
            height = (x[i] - x[i-1]) // 2 + 1
        else:
            height = (x[i] - x[i-1]) // 2
    min_height = max(height, min_height)
print(min_height)