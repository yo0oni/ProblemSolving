import sys
input = sys.stdin.readline

N = int(input())
Want = int(input())
board = [[0] * N for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

ci, cj = N // 2, N // 2
max_count, count, flag = 1, 0, 0
dr = 0
num = 1
board[ci][cj] = 1
while (ci, cj) != (0, 0):
    num += 1
    count += 1

    ci, cj = ci + di[dr], cj + dj[dr]
    board[ci][cj] = num

    if count == max_count:
        count = 0
        dr = (dr+1) % 4

        if flag == 0:
            flag = 1
        else:
            flag = 0
            max_count += 1

for i in range(N):
    print(*board[i])

for i in range(N):
    for j in range(N):
        if board[i][j] == Want:
            print(i+1, j+1)
            break