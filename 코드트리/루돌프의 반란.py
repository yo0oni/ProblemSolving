from collections import deque

N, M, P, C, D = map(int, input().split())
ri, rj = map(lambda x:int(x)-1, input().split())

score = [0] * (P+1)
alive = [1] * (P+1)
alive[0] = 0
wake = [1] * (P+1)

numbers = [[0] * N for _ in range(N)]
numbers[ri][rj]=-1

santa = [[0]*2 for _ in range(P+1)]
for _ in range(1, P+1):
    n, i, j = map(int, input().split())
    numbers[i-1][j-1] = n
    santa[n] = [i-1, j-1]


def move_santa(nn, ii, jj, ddi, ddj, mul):
    dq = [(nn, ii, jj, mul)]

    while dq:
        cur, ci, cj, mul = dq.pop(0)
        ni, nj = ci + ddi*mul, cj + ddj*mul

        if 0 <= ni < N and 0 <= nj < N:
            if numbers[ni][nj] == 0: # 산타가 없으면
                santa[cur] = [ni, nj]
                numbers[ni][nj] = cur
                return
            else:
                dq.append((numbers[ni][nj], ni, nj, 1))
                numbers[ni][nj] = cur
                santa[cur] = [ni, nj]
        else:
            alive[cur] = 0
            return


for turn in range(1, M+1):
    if 1 not in alive:
        break

    # [1] 루돌프 움직임
    r_min = float('inf')
    rs = []
    for num in range(1, P + 1):
        if alive[num] != 1: continue

        si, sj = santa[num]
        dist = (ri - si) ** 2 + (rj - sj) ** 2

        if dist < r_min:
            r_min = dist
            rs = [(santa[num][0], santa[num][1], num)]
        elif dist == r_min:
            rs.append((si, sj, num))

    rs.sort(reverse=True)
    si, sj, snum = rs[0]

    rdi = rdj = 0
    if ri > si:
        rdi = -1  # 산타가 좌표 작은값 => -1방향 이동
    elif ri < si:
        rdi = 1

    if rj > sj:
        rdj = -1
    elif rj < sj:
        rdj = 1

    numbers[ri][rj] = 0
    ri, rj = ri + rdi, rj + rdj
    numbers[ri][rj] = -1

    if (ri, rj) == (si, sj): # 산타랑 충돌하면?
        wake[snum] = turn + 2 # 해당 산타 기절
        score[snum] += C
        move_santa(snum, si, sj, rdi, rdj, C)


    # [2] 산타 움직임
    for num in range(1, P+1):
        if alive[num] == 0: continue
        if wake[num] > turn: continue

        si, sj = santa[num]
        tlst = []
        min_d = (ri-si)**2 + (rj-sj)**2
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = si + di, sj + dj
            dist = (ni - ri) ** 2 + (nj - rj) ** 2

            if 0 <= ni < N and 0 <= nj < N and numbers[ni][nj] <= 0:
                if dist < min_d:
                    min_d = dist
                    tlst.append((ni, nj, di, dj))

        if len(tlst) == 0: continue
        ni, nj, di, dj = tlst[-1]

        if (ni, nj) == (ri, rj): # 충돌이 일어남
            wake[num] = turn + 2
            score[num] += D
            numbers[si][sj] = 0
            move_santa(num, ni, nj, (-1)*di, (-1)*dj, D)

        else:
            numbers[si][sj] = 0
            numbers[ni][nj] = num
            santa[num] = [ni, nj]

    for i in range(1, P+1):
        if alive[i] == 1:
            score[i] += 1

print(*score[1:])