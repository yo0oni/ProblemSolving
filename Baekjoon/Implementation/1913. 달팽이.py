import sys
input = sys.stdin.readline

N = int(input())
Want = int(input())
board = [[0] * N for _ in range(N)]

# 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 반대로?
# 하 우 상 좌

ci, cj = 0, 0
max_count, count, flag = N, 1, 1
dr = 2
num = N*N
board[ci][cj] = N*N
while (ci, cj) != (N//2, N//2):
    num -= 1
    count += 1

    print(ci, cj)
    ci, cj = ci + di[dr], cj + dj[dr]
    board[ci][cj] = num

    if count == max_count:
        count = 0
        dr = (dr-1) % 4

        if flag == 0:
            flag = 1
        else:
            flag = 0
            max_count -= 1

for i in range(N):
    print(*board[i])
