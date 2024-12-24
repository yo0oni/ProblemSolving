import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(r)]
waters = deque()
gosem = deque()

for i in range(r):
    for j in range(c):
        if board[i][j] == "D":
            beber_i, beber_j = i, j
        if board[i][j] == "S":
            gosem.append((i, j))
            board[i][j] = 0
        if board[i][j] == "*":
            waters.append((i, j))

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
visited = [[False for _ in range(c)] for _ in range(r)]

while True:
    new_waters = deque()
    
    for wi, wj in waters:
        for d in range(4):
            nwi, nwj = wi + di[d], wj + dj[d]
        
            if 0 <= nwi < r and 0 <= nwj < c:
                
                if board[nwi][nwj] == ".":
                    board[nwi][nwj] = "*"
                    new_waters.append((nwi, nwj))
                
                if board[nwi][nwj] == ".":
                    board[nwi][nwj] = "*"
                    gosem.remove((nwi, nwj))
    
    waters = new_waters
    can_move = 0
    new_gosem = deque()
    
    for gi, gj in gosem:
        for d in range(4):
            ni, nj = gi + di[d], gj + dj[d]
            
            if 0 <= ni < r and 0 <= nj < c and not visited[ni][nj]:
                if board[ni][nj] == ".":
                    board[ni][nj] = board[gi][gj] + 1
                    visited[ni][nj] = True
                    new_gosem.append((ni, nj))
                    can_move += 1
                                    
                elif board[ni][nj] == "D":
                    print(board[gi][gj] + 1)
                    sys.exit(0)
    
    gosem = new_gosem
            
    if can_move == 0:
        print("KAKTUS")
        break