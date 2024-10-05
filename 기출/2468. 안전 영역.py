import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
max_safe = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 0이 아닌 숫자들이 인접된 칸 확인
def bfs(a, b, visited):
    global graph
    dq = deque([(a, b)])
    visited[a][b] = True
    
    while dq:
        x, y = dq.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx, ny))
    

# 비 내림
def raining(graph, rain):
    for i in range(n):
        for j in range(n):
            if rain != 0:
                graph[i][j] -= 1

for index in range(n):
    graph.append(list(map(int, input().split())))
    max_safe = max(max(graph[index]), max_safe)

safezone = []
zones = []
for rain in range(max_safe+1):
    raining(graph, rain)
    
    visited = [[False] * n for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                count += 1
                
    zones.append(count)

print(max(zones))
