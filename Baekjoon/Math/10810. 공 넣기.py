import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bucket = dict()

for i in range(1, n+1):
    bucket[i] = 0

for _ in range(m):
    i, j, k = map(int, input().split())
    for number in range(i, j+1):
        bucket[number] = k

for value in bucket.values():
    print(value, end=" ")