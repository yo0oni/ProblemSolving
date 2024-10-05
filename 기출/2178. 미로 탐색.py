import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
graph = []


def bfs(a, b):
    distance = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    distance[a][b] = 1
    visited[a][b] = True
    
    dq = deque([(a, b)])
    while dq:
        x, y = dq.popleft()
        
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True 
                    distance[nx][ny] = distance[x][y] + 1
                    dq.append((nx, ny))
        
                    if nx == n-1 and ny == m-1:
                        return distance[nx][ny]
    
    return -1                    
                

for _ in range(n):
    graph.append(list(map(int, input().strip())))

print(bfs(0, 0))