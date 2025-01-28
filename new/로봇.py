import sys
from collections import deque
input = sys.stdin.readline

# 다른 방향으로 틀어야 하면 +1
# 직진하면 +1
# 같은 방향으로 또 직진하면 + 0

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]

si, sj, sd = map(int, input().split())
wi, wj, wd = map(int, input().split())

def change(d):
    if d == 1: # 동쪽
        return 0
    elif d == 2: # 서쪽
        return 2
    elif d == 3: # 남쪽
        return 1
    else: # 북쪽
        return 3

sd = change(sd)
wd = change(wd)

# 동 남 서 북
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj, sd):
    global wi, wj, wd
    dq = deque([(si, sj, sd)])
    
    visited = [[[0] * 4 for _ in range(n)] for _ in range(m)]
    visited[si][sj][sd] = 1
    
    while dq:
        ci, cj, cd = dq.popleft()
        
        if ci == wi and cj == wj and cd == wd:
            return visited[ci][cj][cd]
        
        ni, nj = ci + di[cd], cj + dj[cd]
        if 0 <= ni < m and 0 <= nj < n: # 벽이 아니면
            for i in range(1, 3):
                if board[ci+i][nj] == 0:
                    
            
    
            
        
print(bfs(si-1, sj-1, sd))