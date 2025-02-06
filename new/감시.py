import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

cctv_dirs = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

def watch(temp_board, si, sj, directions):
    for d in directions:
        ci, cj = si, sj
        
        while True:
            ci, cj = ci + di[d], cj + dj[d]
            if not (0 <= ci < n and 0 <= cj < m) or temp_board[ci][cj] == 6:
                break
            if temp_board[ci][cj] == 0:  
                temp_board[ci][cj] = '#'


def dfs(depth, board):
    global answer
    
    if depth == len(cctvs):
        cnt = sum(row.count(0) for row in board)
        answer = min(answer, cnt)
        return

    temp_board = [row[:] for row in board]
    si, sj, cctv_type = cctvs[depth]
    
    for directions in cctv_dirs[cctv_type]:
        watch(temp_board, si, sj, directions)  # CCTV 작동 시뮬레이션
        dfs(depth + 1, temp_board)  # 다음 CCTV 탐색
        temp_board = [row[:] for row in board]  # 원본 복구 (백트래킹)


n, m = map(int, input().split())
board = []
cctvs = []
answer = n * m

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if 1 <= row[j] <= 5:
            cctvs.append((i, j, row[j]))
    board.append(row)

dfs(0, board)
print(answer)
