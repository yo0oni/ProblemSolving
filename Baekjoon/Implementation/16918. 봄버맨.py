import sys
from collections import deque
input = sys.stdin.readline

# 폭탄 위치 구하는 함수
def find_bombs():
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                bombs.append((i, j))

# 전체에 폭탄 채우는 함수
def all_bombs():
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                board[i][j] = 'O'

# 폭탄 터트리는 함수
def explode_bombs():
    while bombs:
        x, y = bombs.popleft()
        board[x][y] = '.'
        # print(x,y)
        # 상하좌우 터트리기, 연쇄 ㄴㄴ
        if x-1 >= 0:
            board[x-1][y] = '.'
        if x+1 < r:
            board[x+1][y] = '.'
        if y-1 >= 0:
            board[x][y-1] = '.'
        if y+1 < c:
            board[x][y+1] = '.'

r, c, n = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

n -= 1
while n>0:
    bombs = deque()
    find_bombs()
    all_bombs()
    n -= 1
    if n == 0:
        break
    explode_bombs()
    n -= 1 
 
for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j], end='')
    print()