import sys, copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def spread_virus(graph, virus):
    dq = deque(virus)
    visited = [[False] * m for _ in range(n)]
    
    while dq:
        x, y = dq.popleft()

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    graph[nx][ny] = 2
                    dq.append([nx, ny])

    return graph

def count_safezone(graph):
    count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1

    return count

def build_wall(graph, locations):
    build_graph = copy.deepcopy(graph)

    for x, y in locations:
        build_graph[x][y] = 1
    
    virus = []
    for i in range(n):
        for j in range(m):
            if build_graph[i][j] == 2:
                virus.append([i, j])

    return spread_virus(build_graph, virus)


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

walls = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            walls.append([i, j])

max_safezone = 0
for locations in combinations(walls, 3):
    result_graph = build_wall(graph, locations)
    
    safezone = count_safezone(result_graph)
    if max_safezone < safezone:
        max_safezone = safezone

print(max_safezone)