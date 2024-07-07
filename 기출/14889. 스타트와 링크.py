import sys
input = sys.stdin.readline

def diff(a, b):
    asum, bsum = 0, 0
    for i in range(n//2):
        for j in range(n//2):
            asum += board[a[i]][a[j]]
            bsum += board[b[i]][b[j]]

    return abs(asum - bsum)

def dfs(depth, a, b):
    global answer
    if depth == n:
        if len(a) == len(b):
            answer = min(answer, diff(a, b))
        return answer

    dfs(depth+1, a+[depth], b)
    dfs(depth+1, a, b+[depth])

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
answer = 1e9
dfs(0, [], [])

print(answer)