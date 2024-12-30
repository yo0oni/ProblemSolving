import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
tomatos = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            tomatos.append((i, j))

di = [0, 1, 0, -1] 
dj = [1, 0, -1, 0]
visited = [[False for _ in range(m)] for _ in range(n)]

while tomatos:
    ti, tj = tomatos.popleft()
    visited[ti][tj] = True
    
    for d in range(4):
        ni, nj = ti + di[d] , tj + dj[d]
        
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
            if board[ni][nj] != -1 and board[ni][nj] == 0:
                board[ni][nj] = board[ti][tj] + 1
                visited[ni][nj] = True
                tomatos.append((ni, nj))

day = 0
flag = False
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            flag = True
        
        day = max(day, board[i][j])

if flag:
    print(-1)
else:   
    print(day - 1)