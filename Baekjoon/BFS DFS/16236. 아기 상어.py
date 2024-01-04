from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
sea = []
shark_size = 2
shark_eat = 0
shark_x, shark_y = 0, 0

for _ in range(n):
    sea.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if sea[i][j] == 9: # 아기 상어
            sea[i][j] = 0
            shark_x = i
            shark_y = j

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def find_fish(sx, sy):
    global shark_size
    queue = deque()
    queue.append([sx, sy])

    visited = [[False for _ in range(n)] for _ in range(n)]
    distance = [[0 for _ in range(n)] for _ in range(n)]
    fish_can_eat = []

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if sea[nx][ny] <= shark_size and not visited[nx][ny]: # 이동 가능
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append([nx, ny])

                    if sea[nx][ny] < shark_size and sea[nx][ny] != 0: # 잡아먹기 가능
                        fish_can_eat.append([nx, ny, distance[nx][ny]])

    fish_can_eat.sort(key = lambda x : (x[2], x[0], x[1]))
    return fish_can_eat


answer = 0
while True:
    fish_list = find_fish(shark_x, shark_y)

    if len(fish_list) == 0:
        print(answer)
        exit(0)

    shark_x, shark_y, time = fish_list[0]
    shark_eat += 1

    if shark_size == shark_eat:
        shark_eat = 0
        shark_size += 1

    sea[shark_x][shark_y] = 0 # 잡아먹은 곳 비어있도록 갱신
    answer += time