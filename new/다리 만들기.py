import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
number = [[0 for _ in range(n)] for _ in range(n)]
ddang = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1: # 육지면
            ddang.append((i, j))

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
num = 1

def give_number(si, sj):
    dq = deque([(si, sj)])
    number[si][sj] = num
    number_visited[si][sj] = True
    
    while dq:
        ci, cj = dq.popleft()
        
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            
            if 0 <= ni < n and 0 <= nj < n and not number_visited[ni][nj]:
                if board[ni][nj] == 1: # 육지면
                    number[ni][nj] = num
                    dq.append((ni, nj))
                    number_visited[ni][nj] = True


# 나라 번호 매기기
number_visited = [[False for _ in range(n)] for _ in range(n)]
for si, sj in ddang:
    if not number_visited[si][sj]:
        give_number(si, sj)
        num += 1


def bfs(si, sj):
    global min_bridge_length
    dq = deque([(si, sj, 0)])
    
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[si][sj] = True
    
    while dq:
        ci, cj, bridge_length = dq.popleft()
        
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                visited[ni][nj] = True
                
                if new_board[ni][nj] == 1 and number[si][sj] != number[ni][nj]:
                    min_bridge_length = min(min_bridge_length, bridge_length)
                
                if new_board[ni][nj] == 0:
                    dq.append((ni, nj, bridge_length + 1))

min_bridge_length = float('inf')
   
for si, sj in ddang:
    new_board = [arr[:] for arr in board]
    bfs(si, sj)

print(min_bridge_length if min_bridge_length != float('inf') else -1)