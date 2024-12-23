from collections import deque
import sys

m, n, h = map(int, input().split())
board = []
for _ in range(h):
    board.append([list(map(int, input().split())) for _ in range(n)])

tomatos = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                tomatos.append((i, j, k))
        

di = [0, 1, 0, -1, 0, 0]
dj = [1, 0, -1, 0, 0, 0]
dk = [0, 0, 0, 0, 1, -1]

while tomatos:
    ci, cj, ck = tomatos.popleft()
    
    for d in range(6):
        ni = ci + di[d]
        nj = cj + dj[d]
        nk = ck + dk[d]
        
        if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m:
            if board[ni][nj][nk] == 0:
                board[ni][nj][nk] = board[ci][cj][ck] + 1
                tomatos.append((ni, nj, nk))
        
max_days = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 0: 
                print(-1)
                sys.exit()
            max_days = max(max_days, board[i][j][k])

print(max_days - 1) 