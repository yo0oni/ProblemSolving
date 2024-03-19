import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    seaList = []

    while q:
        x, y = q.popleft()
        sea = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]: # 바다인 경우
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True

        if sea > 0:
            seaList.append((x, y, sea))

    for x, y, sea in seaList:
        graph[x][y] = max(0, graph[x][y] - sea)

    return 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
year = 0

while ice:
    visited = [[False] * m for _ in range(n)]
    delList = []
    group = 0

    for i, j in ice:
        if graph[i][j] and not visited[i][j]: # 빙산인 경우
            group += bfs(i, j)
        if graph[i][j] == 0: # 탐색 후에 바다가 된 빙산을 체크
            delList.append((i, j))

    if group > 1:
        print(year)
        break

    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if group < 2:
    print(0)
