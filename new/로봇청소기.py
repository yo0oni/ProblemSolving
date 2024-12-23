import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 0 북 1 동 2 남 3 서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
ci, cj = r, c
answer = 0

while True:
    
    if board[ci][cj] == 0:
        board[ci][cj] = -1
        answer += 1
    
    zero = False
    for i in range(4):
        ni, nj = ci + di[i], cj + dj[i]
        
        if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 0:
            zero = True
            break
    
    if not zero:
        ni, nj = ci + di[(d+2)%4], cj + dj[(d+2)%4]
        
        if not (0 <= ni < n and 0 <= nj < m) or board[ni][nj] == 1:
            break
            
        ci, cj = ni, nj
    
    else:
        d = (d-1) % 4
        ni, nj = ci + di[d], cj + dj[d]
        
        if board[ni][nj] == 0 and 0 <= ni < n and 0 <= nj < m:
            ci, cj = ni, nj
    
            
print(answer)