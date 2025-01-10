import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

# 1인데 벽을 한 번도 안뿌셧으면 뿌시고 가기
# 1인데 벽을 뿌셧으면 끝
# 0이면 킵고잉

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj):
    visited =[[[0] * 2 for _ in range(m)] for _ in range(n)]
    dq = deque([(si, sj, 0)])
    visited[si][sj][0] = 1
    
    while dq:
        ci, cj, crashed = dq.popleft()
        
        if ci == n-1 and cj == m-1:
            print(0)
            for i in range(n):
                print(visited[i])
            return visited[ci][cj][crashed]
        
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            
            if 0 <= ni < n and 0 <= nj < m:
                # 벽 x
                if board[ni][nj] == 0 and visited[ni][nj][crashed] == 0:
                    visited[ni][nj][crashed] = visited[ci][cj][crashed] + 1
                    dq.append((ni, nj, crashed))
                    
                # 벽 o
                if board[ni][nj] == 1 and not crashed:
                    visited[ni][nj][1] = visited[ci][cj][crashed] + 1
                    dq.append((ni, nj, 1))
                    
    return -1
                    
    

print(bfs(0, 0))