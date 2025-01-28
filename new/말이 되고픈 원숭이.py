import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

mi = [-1, -2, -2, -1, 1, 2, 2, 1]
mj = [-2, -1, 1, 2, -2, -1, 1, 2]
visited = [[[False for _ in range(k+1)] for _ in range(w)] for _ in range(h)]


def bfs(si, sj):
    dq = deque([(si, sj, k, 0)])
    visited[si][sj][k] = True
    
    while dq:
        ci, cj, k_count, move = dq.popleft()
        
        if ci == h-1 and cj == w-1:
            return move
        
        if k_count: # 말처럼 이동하는 경우
            for m in range(8):
                nmi, nmj = mi[m] + ci, mj[m] + cj

                if 0 <= nmi < h and 0 <= nmj < w and not visited[nmi][nmj][k_count-1]:
                    if board[nmi][nmj] != 1:
                        visited[nmi][nmj][k_count-1] = True
                        dq.append((nmi, nmj, k_count-1, move+1))
        
        for d in range(4):
            ni, nj = di[d] + ci, dj[d] + cj
            
            if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj][k_count]:
                if board[ni][nj] != 1:
                    visited[ni][nj][k_count] = True
                    dq.append((ni, nj, k_count, move+1))
        
    return -1

print(bfs(0, 0))
