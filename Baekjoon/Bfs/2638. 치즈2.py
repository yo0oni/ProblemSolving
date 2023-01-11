import sys
from collections import deque

n,m = map(int,input().split())
chz = [list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    queue = deque()
    queue.append([0,0])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                if chz[nx][ny] >= 1:
                    chz[nx][ny] += 1 # 한번 닿은걸로 안 녹으니까 축적
                else: # 치즈가 아닌 애들만 큐에 들어감
                    visited[nx][ny] = 1
                    queue.append([nx,ny])
                    # if check[nx][ny] == 2:
                    #     chz[nx][ny] = 0
                    # else:
                    #     visited[nx][ny] = 1
                    #     cnt += 1

time = 0
while 1:
    bfs()
    flag = 0
    for i in range(n):
        for j in range(m):
            if chz[i][j] >= 3:
                chz[i][j] = 0
                flag = 1
            elif chz[i][j] == 2:
                chz[i][j] = 1
    if flag == 1:
        time += 1
    else:
        break

print(time)