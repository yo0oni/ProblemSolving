from collections import deque

N, Q = map(int, input().split())
N = 2 ** N
board = [[0]*(N+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(N+2)]
Ls = list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 공격
for L in Ls:
    L = 2**L # L단계

    # 회전
    turn = [[0]*(N+2) for _ in range(N+2)]
    for si in range(1, N + 1, L):
        for sj in range(1, N + 1, L):
            for i in range(L):
                for j in range(L):
                    turn[si + i][sj + j] = board[si + L - 1 - j][sj + i]

    board = turn

    # 얼음 -1
    fuze = [x[:] for x in board]
    for ii in range(1, N + 1):
        for ij in range(1, N + 1):
            if board[ii][ij] == 0:
                continue

            count = 0
            for d in range(4):
                ni, nj = ii + dx[d], ij + dy[d]

                if board[ni][nj] == 0:
                    count += 1

                    if count >= 2:
                        fuze[ii][ij] -= 1
                        break

    board = fuze

remain_ice = 0
max_size_ice = 0

# 남은 얼음 양 세기
find_ice = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if board[i][j] != 0:
            remain_ice += board[i][j]
            find_ice.append((i, j))

visited = [[False] * (N+2) for _ in range(N+2)]

# 가장 큰 얼음 덩어리 찾기
def find_biggest_ice(ii, ij):
    global max_size_ice
    dq = deque()
    dq.append((ii, ij))
    visited[ii][ij] = True
    size = 1

    while dq:
        ci, cj = dq.popleft()

        for i in range(4):
            ni, nj = ci + dx[i], cj + dy[i]

            if board[ni][nj] > 0 and not visited[ni][nj]:
                visited[ni][nj] = True
                dq.append((ni, nj))
                size += 1

    max_size_ice = max(max_size_ice, size)

# 가장 큰 얼음 찾기
for i, j in find_ice:
    find_biggest_ice(i, j)

print(remain_ice)
print(max_size_ice)