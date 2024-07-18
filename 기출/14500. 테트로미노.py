import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

max_value = 0
def dfs(depth, value, x, y):
    global max_value

    if depth == 4:
        max_value = max(max_value, value)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(depth+1, value + board[ny][nx], nx, ny)
            visited[ny][nx] = False

def other_dfs(x, y):
    global max_value
    queue = []

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            queue.append(board[ny][nx])

    length = len(queue)
    if length == 4:
        queue.sort(reverse=True)
        queue.pop()
        max_value = max(max_value, sum(queue) + board[y][x])

    elif length == 3:
        max_value = max(max_value, sum(queue) + board[y][x])

    return

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(1, board[i][j], j, i)
        other_dfs(j, i)
        visited[i][j] = False

print(max_value)