import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
bings = []
for i in range(n):
    for j in range(m):
        if board[i][j] != 0:
            bings.append((i, j))

if len(bings) <= 1:
    print(0)
    sys.exit(0)
    
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

time = 0

def bfs(si, sj):
    dq = deque([(si, sj)])
    visited[si][sj] = True
    
    while dq:
        ci, cj = dq.popleft()
        
        for d in range(4):
            ni, nj = di[d] + ci, dj[d] + cj
            
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if board[ni][nj] > 0: # 빙하면
                    dq.append((ni, nj))
                    visited[ni][nj] = True



while True:
    visited = [[False] * m for _ in range(n)]
    count = 0
    
    for bi, bj in bings:
        if not visited[bi][bj]:
            # 덩어리 개수 세기
            bfs(bi, bj)
            count += 1
    
    if count >= 2:
        print(time)
        break
    
    # 빙하 녹기
    count_board = [[0 for _ in range(m)] for _ in range(n)]
    for bi, bj in bings:
        for d in range(4):
            ni, nj = bi + di[d], bj + dj[d]
            if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 0:
                count_board[bi][bj] += 1
        
    for bi, bj in bings:
        board[bi][bj] = max(0, board[bi][bj] - count_board[bi][bj])
    
    bings = []
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                bings.append((i, j))
    
    if len(bings) <= 1:
        print(0)
        sys.exit(0)
                
    time += 1