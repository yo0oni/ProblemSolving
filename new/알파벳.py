import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(r)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
alphabets = set()
max_length = 0

def dfs(ci, cj, length):
    global max_length
    
    max_length = max(max_length, length)
    alphabets.add(board[ci][cj])
    
    for d in range(4):
        ni = di[d] + ci
        nj = dj[d] + cj
        
        if 0 <= ni < r and 0 <= nj < c and board[ni][nj] not in alphabets:
            dfs(ni, nj, length + 1)
            
    alphabets.remove(board[ci][cj])
    
dfs(0, 0, 1)
print(max_length)