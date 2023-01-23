import sys
from collections import deque

n,m = map(int,input().split())
ice = []
for i in range(n):
    ice.append(list(map(int,sys.stdin.readline().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
#
# 다 녹았으면(두 덩어리로 나뉘는 게 불가능한 것이니까) 0을 출력하고 break
# 1-2) 빙산이 다 녹지 않았으면 1년 더 (year에 1을 추가하고, melt())

def bfs(x_, y_):
    dq = deque()
    dq.append([x_,y_])
    visited[x_][y_] = 1
    # 동서남북이 0인게 하나라도 있으면 분리된 거임!!!!
    while dq:
        count = 0
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if ice[nx][ny] == 0:    # 빙산이 없는경우 +1 해준다
                    minus[(x, y)] += 1
                elif ice[nx][ny] != 0 and visited[nx][ny] == 0:  # 빙산인데 방문하지 않은경우 append시켜줌
                    dq.append([nx,ny])
                    visited[nx][ny] = 1
                    
year = 0
while 1:
    lump = 0
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0 and visited[i][j] == False:
                bfs(i, j)
                lump += 1
    year += 1
    if lump >= 2:
        print(year-1)
        break
    elif lump == 0:
        print(0)
        break