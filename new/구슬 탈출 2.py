import sys
from collections import deque
input = sys.stdin.readline

# 빨, 파 구슬 있는데 빨간 구슬만 빼내기
# 상하좌우로 굴리기 가능

# 빨, 파 동시에 빠지면 실패
# 파랑 빠져도 실패
# 무조건 빨강만 빠져야됨

# 기울이는 동작은 구슬이 움직이지 못할 때까지 계속
# 10번 이하로 빨간 구슬을 빼낼 수 없으면 -1 출력

# 풀이
# 한 칸만 움직이는게 아니라 벽에 부딪힐 때까지 굴러감
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def move(si, sj, d):
    count = 0
    
    while True:
        si, sj = si + di[d], sj + dj[d]
        if board[si][sj] == "#" or board[si][sj] == "0":
            break
        count += 1
            
    return si, sj, count


def bfs(ri, rj,  bi, bj):
    visited = set()
    visited.add((ri, rj, bi, bj))
    dq = deque([(ri, rj, bi, bj, 0)])
    
    while dq:
        cri, crj, cbi, cbj, count = dq.popleft()
        
        if count > 10:
            return -1
        
        for d in range(4):
            nri, nrj, rcnt = move(cri, crj, d)
            nbi, nbj, bcnt = move(cbi, cbj, d)

            if board[nbi][nbj] == "0":
                continue
            
            if board[nri][nrj] == "0":
                return count + 1

            if (nri, nrj) == (nbi, nbj):
                if rcnt > bcnt:
                    nri, nrj = nri - di[d], nrj - dj[d]
                else:
                    nbi, nbj = nbi - di[d], nbj - dj[d]

            if (nri, nrj, nbi, nbj) not in visited:
                visited.add((nri, nrj, nbi, nbj))
                dq.append((nri, nrj, nbi, nbj, count+1))
        
    return -1


n, m = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(n)]
ri, rj = 0, 0
bi, bj = 0, 0

for i in range(n):
    for j in range(m):
        if board[i][j] == "R":
            ri, rj = i, j
            board[ri][rj] = "."
        elif board[i][j] == "B":
            bi, bj = i, j
            board[bi][bj] = "."
            
print(bfs(ri, rj, bi, bj))