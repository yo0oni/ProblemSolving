import sys, copy
input = sys.stdin.readline

def move(board, d):
    if d == 0: # 위
        for y in range(n):
            end = 0
            for x in range(1, n):
                if board[x][y]:
                    tmp = board[x][y]
                    board[x][y] = 0
                    if board[end][y] == 0:
                        board[end][y] = tmp
                    elif board[end][y] == tmp:
                        board[end][y] *= 2
                        end += 1
                    else:
                        end += 1
                        board[end][y] = tmp
    if d == 1: # 아래
        for y in range(n):
            end = n-1
            for x in range(n-2, -1, -1):
                if board[x][y]:
                    tmp = board[x][y]
                    board[x][y] = 0
                    if board[end][y] == 0:
                        board[end][y] = tmp
                    elif board[end][y] == tmp:
                        board[end][y] *= 2
                        end -= 1
                    else:
                        end -= 1
                        board[end][y] = tmp
    if d == 2: # 왼쪽
        for x in range(n):
            end = 0
            for y in range(1, n):
                if board[x][y]:
                    tmp = board[x][y]
                    board[x][y] = 0
                    if board[x][end] == 0:
                        board[x][end] = tmp
                    elif board[x][end] == tmp:
                        board[x][end] *= 2
                        end += 1
                    else:
                        end += 1
                        board[x][end] = tmp
                        
    if d == 3: # 오른쪽
        for x in range(n):
            end = n-1
            for y in range(n-2, -1, -1):
                if board[x][y]:
                    tmp = board[x][y]
                    board[x][y] = 0
                    if board[x][end] == 0:
                        board[x][end] = tmp
                    elif board[x][end] == tmp:
                        board[x][end] *= 2
                        end -= 1
                    else:
                        end -= 1
                        board[x][end] = tmp
        
    return board


def find_max(board):
    max_value = 0
    
    for i in range(n):
        for j in range(n):
            max_value = max(max_value, board[i][j])
    
    return max_value
            

def dfs(board, depth):
    global answer
    
    if depth == 5:
        answer = max(answer, find_max(board))
        return
    
    # 0상 1하 2좌 3우
    for d in range(4):
        after_move = move(copy.deepcopy(board), d)
        dfs(after_move, depth+1)
        
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dfs(board, 0)
print(answer)