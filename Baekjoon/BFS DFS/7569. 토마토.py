from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
tomatos = []
queue = deque([])

for i in range(h):
    tomato = []
    for j in range(n):
        tomato.append(list(map(int, input().split())))
        for k in range(m):
            if tomato[j][k] == 1:
                queue.append([i, j, k])

    tomatos.append(tomato)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while queue:
    x, y, z = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and tomatos[nx][ny][nz] == 0:
            queue.append([nx, ny, nz])
            tomatos[nx][ny][nz] = tomatos[x][y][z] + 1

day = 0
for i in tomatos:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
                
        day = max(day, max(j))

print(day - 1)