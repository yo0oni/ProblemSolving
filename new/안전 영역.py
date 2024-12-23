import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

max_height = 0
for i in range(n):
    for j in range(n):
        if board[i][j] > max_height:
            max_height = board[i][j]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj):
    global visited, rain_board
    dq = deque([(si, sj)])
    visited[si][sj] = True
    
    while dq:
        ci, cj = dq.popleft()
        
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if rain_board[ni][nj]:
                    visited[ni][nj] = True
                    dq.append((ni, nj))
    


max_count = 0
for height in range(max_height):
    visited = [[False for _ in range(n)] for _ in range(n)]
    rain_board = [[True for _ in range(n)] for _ in range(n)]

    # 비 내리기
    for i in range(n):
        for j in range(n):
            if board[i][j] <= height:
                rain_board[i][j] = False # 잠김
    
    # 안전 영역 세기
    count = 0
    for i in range(n):
        for j in range(n):
            if rain_board[i][j] and not visited[i][j]: # 살아있으면
                bfs(i, j)
                count += 1
                
    max_count = max(max_count, count)

print(max_count)