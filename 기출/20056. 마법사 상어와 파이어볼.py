n, m, k = map(int, input().split())
balls = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    balls[r-1][c-1].append([m, s, d])

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]


for _ in range(k):
    new_balls = [[[] for _ in range(n)] for _ in range(n)]

    # 이동
    for bi in range(n):
        for bj in range(n):
            if balls[bi][bj]:
                for m, s, d in balls[bi][bj]:
                    ni, nj = (bi + di[d] * s) % n, (bj + dj[d] * s) % n
                    new_balls[ni][nj].append([m, s, d])

    # 합치기
    for bi in range(n):
        for bj in range(n):
            length = len(new_balls[bi][bj])

            if length >= 2:
                sm, ss, odd_s, even_s = 0, 0, 0, 0

                for m, s, d in new_balls[bi][bj]:
                    sm += m
                    ss += s
                    if d % 2 != 0:
                        odd_s += 1
                    else:
                        even_s += 1

                sm //= 5
                ss //= length

                if sm == 0:
                    new_balls[bi][bj] = []
                    continue

                if odd_s == length or even_s == length: # 다 홀수 or 짝수
                    new_balls[bi][bj] = []
                    for new_d in [0, 2, 4, 6]:
                        new_balls[bi][bj].append([sm, ss, new_d])

                else:
                    new_balls[bi][bj] = []
                    for new_d in [1, 3, 5, 7]:
                        new_balls[bi][bj].append([sm, ss, new_d])

    balls = [row[:] for row in new_balls]

answer = 0
for i in range(n):
    for j in range(n):
        if balls[i][j]:
            for ball in balls[i][j]:
                answer += ball[0]
print(answer)