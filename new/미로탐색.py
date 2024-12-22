import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj):
    visited = [[False] * m for _ in range(n)]
    dq = deque([(si, sj)])
    
    while dq:
        ci, cj = dq.popleft()
        
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if board[ni][nj] != 0: # 이동 가능하면
                    board[ni][nj] += board[ci][cj]
                    dq.append((ni, nj))
                    visited[ni][nj] = True
    
    return board[n-1][m-1]
    
print(bfs(0, 0))