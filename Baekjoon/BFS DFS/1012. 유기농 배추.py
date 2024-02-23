import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dertermine_earthworms(graph, search_list):
    visited = [[False] * n for _ in range(m)]
    count = 0

    for x, y in search_list:
        if visited[x][y]:
            continue
        dq = deque([(x, y)])

        while dq:
            x, y = dq.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if graph[nx][ny] == 1:
                        visited[nx][ny] = True
                        dq.append([nx, ny])

        count += 1
        
    return count

for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for i in range(m)]
    search_list = []

    for _ in range(k):
        row, col = map(int, input().split())
        graph[row][col] = 1
        search_list.append([row, col])
    print(dertermine_earthworms(graph, search_list))