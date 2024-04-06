import sys
input = sys.stdin.readline

n = int(input())
board = [list(input().strip()) for _ in range(n)]

def check_eat():
    can_eat = 0

    for i in range(n):
        c_count, p_count, z_count, y_count = 0, 0, 0, 0

        for j in range(n):
            if board[i][j] == 'C':
                c_count += 1
                p_count, z_count, y_count = 0, 0, 0
            elif board[i][j] == 'P':
                p_count += 1
                c_count, z_count, y_count = 0, 0, 0
            elif board[i][j] == 'Z':
                z_count += 1
                c_count, p_count, y_count = 0, 0, 0
            else:
                y_count += 1
                c_count, z_count, p_count = 0, 0, 0

            can_eat = max(can_eat, c_count, p_count, z_count, y_count)

    for i in range(n):
        c_count, p_count, z_count, y_count = 0, 0, 0, 0

        for j in range(n):
            if board[j][i] == 'C':
                c_count += 1
                p_count, z_count, y_count = 0, 0, 0
            elif board[j][i] == 'P':
                p_count += 1
                c_count, z_count, y_count = 0, 0, 0
            elif board[j][i] == 'Z':
                z_count += 1
                c_count, p_count, y_count = 0, 0, 0
            else:
                y_count += 1
                c_count, z_count, p_count = 0, 0, 0
        
            can_eat = max(can_eat, c_count, p_count, z_count, y_count)
    
    return can_eat

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

max_eat = 0
for i in range(n):
    for j in range(n):
        origin = board[i][j]

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if origin != board[nx][ny]:
                    board[i][j], board[nx][ny] = board[nx][ny], origin
                    max_eat = max(max_eat, check_eat())
                    board[nx][ny], board[i][j] = board[i][j], origin

print(max_eat)