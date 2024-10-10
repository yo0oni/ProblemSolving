import sys
input = sys.stdin.readline

# 숲의 동쪽, 서쪽, 남쪽은 마법의 벽으로 막혀 있으며
# 정령들은 숲의 북쪽을 통해서만 숲에 들어올 수 있습니다.

# 총 K명의 정령은 각자 골렘을 타고 숲을 탐색
# 각 골렘은 십자 모양의 구조
# 중앙 칸을 포함해 총 5칸을 차지합니다 (중앙 + 상하좌우)
# 골렘의 중앙을 제외한 4칸 중 한 칸은 골렘의 출구

# i번째 골렘은 골렘의 중앙이 ci열이 되도록 하는 위치에서 내려옴
# 초기 골렘의 출구는 di의 방향에 위치해 있습니다.

dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

south = [(1, -1), (2, 0), (1, 1)]
west = [(-1, -1), (0, -2), (1, -1), (1, -2), (2, -1)]
east = [(-1, 1), (0, 2), (1, 1), (2, 1), (1, 2)]

R, C, K = map(int, input().split())
Golrem = [list(map(int, input().split())) for _ in range(K)]
board = [[0]*(C+2) for _ in range(3)] + [[-1] + [0] * C + [-1] for _ in range(R)] + [[-1]*(C+2)]


answer = 0
num = 1
for c, d in Golrem: # 출발하는 열, 출구 방향
    ci, cj = 2, c

    # 맨 밑까지 도착할 때까지 반복
    while True:
        count = 0
        for di, dj in south:
            count += board[ci + di][cj + dj]

        if count == 0: # 남쪽 ㄱㄴ
            ci += 1
            continue

        count = 0
        for di, dj in west:
            count += board[ci + di][cj + dj]

        if count == 0: # 서쪽 후 남쪽 ㄱㄴ
            ci += 1
            cj -= 1
            d = (d - 1) % 4  # 출구 반시계 회전
            continue

        count = 0
        for di, dj in east:
            count += board[ci + di][cj + dj]

        if count == 0: # 동쪽 후 남쪽 ㄱㄴ
            ci += 1
            cj += 1
            d = (d + 1) % 4 # 출구 시계 회전
            continue

        # 다 안되면 끝
        else:
            break

    # [4] 더이상 내려갈 수 없으면
    # 만약 일부가 밖으로 빠져나가 있으면? -- 중앙의 ci가 3 이하면
    if ci <= 3:
        board = [[0]*(C+2) for _ in range(3)] + [[-1] + [0] * C + [-1] for _ in range(R)] + [[-1]*(C+2)]
        num += 1
        continue

    else: # 만약 안에 잘 들어가 있으면?
        board[ci][cj] = ci - 1
        for i, j in dr:
            ni, nj = ci + i, cj + j
            board[ni][nj] = ci - 1

        oi, oj = ci + dr[d][0], cj + dr[d][1] # 출구 좌표
        max_under = board[oi][oj]
        for i, j in dr:
            ni, nj = oi + i, oj + j
            max_under = max(board[ni][nj], max_under)

        board[ci][cj] = max_under
        for i, j in dr:
            ni, nj = ci + i, cj + j
            board[ni][nj] = max_under
        max_under = 0

        answer += board[ci][cj]

print(answer)