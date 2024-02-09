import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
total_v_count = 0
total_o_count = 0
graph = []

for _ in range(r):
    data = list(map(str, input().strip()))
    total_v_count += data.count('v')
    total_o_count += data.count('o')
    graph.append(data)

o_locations = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'o':
            o_locations.append([i, j])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dq = deque()
visited = [[False] * c for _ in range(r)]

for location in o_locations:
    dq.append(location)
    v_count = 0
    o_count = 1
    
    while dq: 
        x, y = dq.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == '#':
                    continue

                elif graph[nx][ny] == 'v':
                    v_count += 1
                    graph[nx][ny] = '.'

                elif graph[nx][ny] == 'o':
                    o_count += 1
                    graph[nx][ny] = '.'
                    
                dq.append([nx, ny])
                
    if o_count <= v_count:
        total_o_count -= o_count
    else:
        total_v_count -= v_count
    
print(total_o_count, total_v_count)