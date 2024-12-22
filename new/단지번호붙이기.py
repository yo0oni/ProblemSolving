import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]
is_home = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            is_home.append((i, j))
            
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj):
    global visited
    count = 1
    dq = deque([(si, sj)])
    visited[si][sj] = True
    
    while dq:
        ci, cj = dq.popleft()
        
        for d in range(4):
            ni, nj = di[d] + ci, dj[d] + cj
            
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                visited[ni][nj] = True
                
                if board[ni][nj] == 1: # 집이면
                    count += 1
                    dq.append((ni, nj))
    
    return count
                    

visited = [[False] * n for _ in range(n)]
dange = 0
counts = []
for si, sj in is_home:
    if not visited[si][sj]:
        counts.append(bfs(si, sj))
        dange += 1

counts.sort()
print(dange)
for count in counts:
    print(count)