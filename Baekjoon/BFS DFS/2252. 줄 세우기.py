from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int,input().rstrip().split())

students = [[] for _ in range(N + 1)]
count = [0 for _ in range(N + 1)]
que = deque()

for i in range(M):
    x, y = map(int,input().rstrip().split())
    students[x].append(y)
    count[y] += 1

for i in range(1, N + 1):
    if count[i] == 0:
        que.append(i)

while que:
    short = que.popleft()
    print(short, end=' ')

    for student in students[short]:
        count[student] -= 1
        if count[student] == 0:
            que.append(student)