import sys
input = sys.stdin.readline

def check_bomb():
    for i in range(r):
        for j in range(c):
            if board[i][j] == "O":
                bomb_location.append((i, j))

def plant_bomb_all():
    for i in range(r):
        for j in range(c):
            if board[i][j] == ".":
                board[i][j] = "O"

def explode_bomb():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    global bomb_location
    
    for x, y in bomb_location:
        board[x][y] = "."

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                board[nx][ny] = "."
    

r, c, n = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
time = 1

while time < n:
    bomb_location = []
    check_bomb()
    plant_bomb_all()
    time += 1
    
    if time < n:
        explode_bomb()
    time += 1

for i in range(r):
    for j in range(c):
        print(board[i][j], end="")
    print()