import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[False]*m for _ in range(n)]
dq = deque()

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            dq.append([i, j])
            graph[i][j] = 0
            visited[i][j] = True

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while dq:
    x, y = dq.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if graph[nx][ny] == 1:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                dq.append([nx, ny])
            elif graph[nx][ny] == 0:
                visited[nx][ny] = True

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            graph[i][j] = -1

for i in range(n):
    print(*graph[i])