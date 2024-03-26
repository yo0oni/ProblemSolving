import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(graph, cabbages):
    count = 0
    visited = [[False] * n for _ in range(m)]

    for x, y in cabbages:
        if not visited[x][y]:
            dq = deque([(x, y)])
            visited[x][y] = True

            while dq:
                x, y = dq.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        if graph[nx][ny] == 1:
                            visited[nx][ny] = True
                            dq.append((nx, ny))
            
            count += 1
    
    return count


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    cabbages = []
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                cabbages.append((i, j))

    print(bfs(graph, cabbages))