import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(a, b):
    global visited
    dq = deque([(a, b)])
    visited[a][b] = True
    count = 1
    
    while dq:
        x, y = dq.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                
                if graph[nx][ny] == 1:
                    dq.append((nx, ny))
                    count += 1
                    
    return count


n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().strip())))

houses = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append([i, j])

visited = [[False] * n for _ in range(n)]
groups = []
for i, j in houses:
    if not visited[i][j]:
        groups.append(bfs(i, j))

groups.sort()
print(len(groups))
for index in range(len(groups)):
    print(groups[index])