import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j])

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append([nx, ny])

ans = 0
for line in arr:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()

    ans = max(ans, max(line))

print(ans-1)