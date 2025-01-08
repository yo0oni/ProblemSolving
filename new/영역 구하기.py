import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    
    for x in range(sx, ex):
        for y in range(sy, ey):
            board[y][x] = -1

new_board = deque()
for i in range(m):
    new_board.appendleft(board[i])
    
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj):
    size = 1
    dq = deque([(si, sj)])
    visited[si][sj] = True
    
    while dq:
        ci, cj = dq.popleft()
        
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
        
            if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                if new_board[ni][nj] == 0:
                    visited[ni][nj] = True
                    dq.append((ni, nj))
                    size += 1
    
    return size
        
no_square = []
for i in range(m):
    for j in range(n):
        if new_board[i][j] == 0:
            no_square.append((i, j))
            
visited = [[False for _ in range(n)] for _ in range(m)]
count = 0
answer = []
for si, sj in no_square:
    if not visited[si][sj]:
        count += 1
        answer.append(bfs(si, sj))

answer.sort()
print(count)
print(*answer)