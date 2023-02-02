# 칸마다 숫자 기입
# 2x2가 될때까지 자르기

N, R, C = map(int,input().split())
res = 0
# print(n,r,c)
# number = -1
# paper = [[0]*2**n for _ in range(2**n)]

# for i in range(2**n):
#     for j in range(2**n):
#         number += 1
#         paper[i][j] = number

# print(paper)

# 3 7 7
# N R C

def visited(n, r, c): # 8 0 0
    global res

    # print("tt", n)
    # 찾는 좌표라면 res를 출력하고 종료
    if r == R and c == C:
        print(int(res))
        exit(0)

    # 찾는 좌표가 없다면 res에 크기를 더하기
    if not (r <= R < r + n and c <= C < c + n):
        res += n * n
        print(res)

        return

    # 1/2/3/4사분면을 재귀적으로 탐색
    visited(n/2, r, c) # 1사분면
    visited(n/2, r, c + n/2) # 2사분면
    visited(n/2, r + n/2, c) # 3사분면
    visited(n/2, r + n/2, c + n/2) # 4사분면


# 2^n을 0, 0부터 탐색
visited(2 ** N, 0, 0)