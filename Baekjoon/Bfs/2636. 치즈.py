import sys
from collections import deque

n,m = map(int,input().split())
chz = []
for i in range(n):
    chz.append(list(map(int,sys.stdin.readline().split().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = []

def bfs():
    queue = deque()
    queue.append([0,0])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    cnt = 0

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                if chz[nx][ny] == 0:
                    visited[nx][ny] = 1
                    # 치즈 아닌 애들 추가
                    queue.append([nx,ny])
                elif chz[nx][ny] == 1:
                    chz[nx][ny] = 0 # 치즈니까 녹음
                    visited[nx][ny] = 1
                    cnt += 1
    ans.append(cnt)
    return cnt

time = 0
while 1:
    time +=1
    cnt = bfs() 
    if cnt == 0:
        break

print(time-1)
print(ans[-2])