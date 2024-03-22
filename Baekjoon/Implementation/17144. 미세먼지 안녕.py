import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solve(r, c, t, board):
    # 공기청정기 위치 찾기
    cleaner = []
    for i in range(r):
        if board[i][0] == -1:
            cleaner.append((i, 0))

    # 미세먼지 확산
    def difussion():
        global board
        calculate = [[0] * c for _ in range(r)]

        for x in range(r):
            for y in range(c):
                count = 0
                if board[x][y] > 0:
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if 0 <= nx < r and 0 <= ny < c:
                            if board[nx][ny] != -1:
                                calculate[nx][ny] += board[x][y] // 5
                                count += 1
                            
                    calculate[x][y] -= (count * (board[x][y] // 5))
                
        for i in range(r):
            for j in range(c):
                board[i][j] += calculate[i][j]

    def freshing():
        # 공기청정기 위쪽 작동
        global board
        i, j = cleaner[0]
        temp = 0
        
        while 0 <= j + 1 < c:
            temp, board[i][j + 1] = board[i][j + 1], temp
            j += 1
        while 0 <= i - 1 < r:
            temp, board[i - 1][j] = board[i - 1][j], temp
            i -= 1
        while 0 <= j - 1 < c:
            temp, board[i][j - 1] = board[i][j - 1], temp
            j -= 1
        while 0 <= i + 1 < r and board[i + 1][j] != -1:
            temp, board[i + 1][j] = board[i + 1][j], temp
            i += 1
        
        # 아래 공기청정기 순환
        i, j = cleaner[1]
        temp = 0

        while 0 <= j + 1 < c:
            temp, board[i][j + 1] = board[i][j + 1], temp
            j += 1
        while 0 <= i + 1 < r:
            temp, board[i + 1][j] = board[i + 1][j], temp
            i += 1
        while 0 <= j - 1 < c:
            temp, board[i][j - 1] = board[i][j - 1], temp
            j -= 1
        while 0 <= i - 1 < r and board[i - 1][j] != -1:
            temp, board[i - 1][j] = board[i - 1][j], temp
            i -= 1

    def result():
        answer = 0
        for i in range(r):
            for j in range(c):
                if board[i][j] > 0:
                    answer += board[i][j]
        return answer
                    
    for _ in range(t):
        difussion()
        freshing()
    return result()

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
print(solve(r, c, t, board))