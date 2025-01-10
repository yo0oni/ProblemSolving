import sys
from collections import deque
input = sys.stdin.readline

# 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고
# 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.

board = [list(map(str, input().strip())) for _ in range(12)]
    
# 시작
# 뿌요 위치 저장

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj, color):
    dq = deque([(si, sj)])
    visited[si][sj] = True
    count = 1
    delete = [(si, sj)]
    
    while dq:
        ci, cj = dq.popleft()
        
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            
            if 0 <= ni < 12 and 0 <= nj < 6 and not visited[ni][nj]:
                if color == board[ni][nj]:
                    count += 1
                    delete.append((ni, nj))
                    visited[ni][nj] = True
                    dq.append((ni, nj))
                    
    if count >= 4:
        return delete
    return None
                

answer = 0
while True:
    puyos = []
    
    for i in range(12):
        for j in range(6):
            if board[i][j] != ".":
                puyos.append((i, j, board[i][j]))
    
    visited = [[False for _ in range(6)] for _ in range(12)]
    to_delete = []
    for pi, pj, color in puyos:
        if not visited[pi][pj]:
            coordinate = bfs(pi, pj, color)
            if coordinate != None:
                to_delete += coordinate
            
    if len(to_delete) == 0:
        print(answer)
        break
    
    for pi, pj in to_delete:
        board[pi][pj] = "."
        
    answer += 1
    
    for j in range(6):
        for i in range(10, -1, -1):
            for k in range(11, i, -1):
                if board[i][j] != "." and board[k][j] == ".":
                    board[k][j] = board[i][j]
                    board[i][j] = "."
    