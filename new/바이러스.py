import sys
from collections import deque
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj, n, m, board):
    dq = deque([(si, sj, 0)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[si][sj] = True
    
    max_distance = 0
    
    while dq:
        ci, cj, cd = dq.popleft()
        
        if max_distance < cd:
            max_distance = cd
    
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if board[ni][nj] == "L":
                    visited[ni][nj] = True
                    dq.append((ni, nj, cd+1))
    
    return max_distance


def main():
    n, m = map(int, input().split())
    board = [list(map(str, input().strip())) for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(m):
            if 0 <= i-1 and i+1 < n and board[i-1][j] == "L" and board[i+1][j] == "L":
                continue
            if 0 <= j-1 and j+1 < m and board[i][j-1] == "L" and board[i][j+1] == "L":
                continue
            if board[i][j] == "L":
                answer = max(answer, bfs(i, j, n, m, board))

    
    print(answer)

if __name__ == "__main__":
    main()