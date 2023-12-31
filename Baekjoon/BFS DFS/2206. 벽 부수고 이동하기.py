from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b, c) :
    q = deque()
    q.append((a, b, c))

    while q :
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1 :
            return visited[x][y][z]

        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < n and 0 <= ny < m) :
                continue

            if data[nx][ny] == 1 and z == 0 :
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append((nx, ny, 1))

            elif data[nx][ny] == 0 and visited[nx][ny][z] == 0 :
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))

    return -1

print(bfs(0, 0, 0))