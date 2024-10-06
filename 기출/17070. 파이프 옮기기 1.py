import sys
input = sys.stdin.readline

# dfs로 풀어야된다.
# 이유 : 갈 수 있는 방법을 모두 동원
# 가로 -> 대각선 or 가로
# 세로 -> 대각선 or 세로
# 대각선 -> 대각선 or 가로 or 세로

def dfs(x, y, direction):
    global count
    
    if (x, y) == (n, n):
        count += 1
        return
    
    # 가로
    if direction == 1:
        # 가로
        if graph[x][y+1] == 0:
            dfs(x, y+1, 1)
        # 대각선
        if graph[x+1][y+1] == 0 and graph[x+1][y] == 0 and graph[x][y+1] == 0:
            dfs(x+1, y+1, 3)
    
    # 세로
    elif direction == 2:
        # 세로
        if graph[x+1][y] == 0:
            dfs(x+1, y, 2)
        # 대각선
        if graph[x+1][y+1] == 0 and graph[x+1][y] == 0 and graph[x][y+1] == 0:
            dfs(x+1, y+1, 3)
    
    # 대각선
    else:
        # 가로
        if graph[x][y+1] == 0:
            dfs(x, y+1, 1)
        #세로
        if graph[x+1][y] == 0:
            dfs(x+1, y, 2)
        # 대각선
        if graph[x+1][y+1] == 0 and graph[x+1][y] == 0 and graph[x][y+1] == 0:
            dfs(x+1, y+1, 3)
            
    return count


n = int(input())
graph = [[1] * (n+2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(n)] + [[1] * (n+2)]
count = 0

print(dfs(1, 2, 1)) # 끝점을 기준으로 판단
