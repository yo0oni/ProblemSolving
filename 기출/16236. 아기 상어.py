import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def find_fish(shark_x, shark_y):
    global shark_size

    visited = [[False] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    fish_can_eat = []

    dq = deque([(shark_x, shark_y)])

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] <= shark_size:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    dq.append([nx, ny])

                    if graph[nx][ny] != 0 and graph[nx][ny] < shark_size:
                        fish_can_eat.append([nx, ny, distance[nx][ny]])

    fish_can_eat.sort(key = lambda x : (x[2], x[0], x[1]))
    return fish_can_eat


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
shark_x, shark_y = 0, 0
shark_size, shark_eat = 2, 0
total_time = 0
fish_list = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            graph[i][j] = 0

while True:
    fish_list = find_fish(shark_x, shark_y)
    
    if len(fish_list) == 0:
        break

    shark_x, shark_y, time = fish_list[0]
    shark_eat += 1

    if shark_size == shark_eat:
        shark_eat = 0
        shark_size += 1

    graph[shark_x][shark_y] = 0
    total_time += time

print(total_time)