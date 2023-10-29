import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

def bfs(x, y):
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 넘어가면 끝
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            # 0인경우 지나갈 수 없는 길
            if graph[nx][ny] == 0:
                continue
            
            # 이때만 가능! 지금까지 이동한 횟수 더한 후 이어서 계속하기
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
        
    return graph[N-1][M-1]

print(bfs(0, 0))