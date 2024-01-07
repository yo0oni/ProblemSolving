from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().strip())))

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b, c):
    queue = deque()
    queue.append((a, b, c))

    while queue:
        x, y, z = queue.popleft()

        if x == n - 1 and y == m - 1: # 끝에 도달
            return visited[x][y][z] # 최종 거리 출력

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1 # 거리 갱신
                    queue.append((nx, ny, 1))

                elif data[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1 # 거리 갱신
                    queue.append((nx, ny, z))

    return -1

print(bfs(0, 0, 0))