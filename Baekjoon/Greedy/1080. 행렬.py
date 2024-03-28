import sys
input = sys.stdin.readline

def change(i, j, a):
    for x in range(i, i+3):
        for y in range(j, j+3):
            a[x][y] = 1 - a[x][y]

def compare():
    count = 0

    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                change(i, j, a)
                count += 1
    
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return -1
    
    return count

n, m = map(int, input().split())
a = [list(map(int, input().strip())) for _ in range(n)]
b = [list(map(int, input().strip())) for _ in range(n)]

print(compare())