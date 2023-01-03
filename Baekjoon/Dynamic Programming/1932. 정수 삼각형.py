import sys

n = int(input())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n): # 1, 2, 3, 4
    for j in range(0, i+1): # 0, 1, 2, 3, 4
        if j == 0:
            # i == 2 , j == 0
            l[i][j] = l[i-1][j] + l[i][j]
        elif i == j:
            # i == 1 , j == 1
            l[i][j] = l[i-1][j-1] + l[i][j]
        else:
            # i == 2, j == 1
            # i == 4, j == 2
            l[i][j] = max(l[i-1][j-1], l[i-1][j]) + l[i][j]

print(max(l[n-1]))