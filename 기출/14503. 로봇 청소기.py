import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    if graph[r][c] == 0:
        graph[r][c] = -1 # 청소

    count = 0
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                count += 1


    if count != 0:
        d = (d - 1) % 4
        if 0 <= r + dx[d] < n and 0 <= c + dy[d] < m and graph[r + dx[d]][c + dy[d]] == 0:
            r += dx[d]
            c += dy[d]
    
    else:
        back_d = (d + 2) % 4
        if 0 <= r + dx[back_d] < n and 0 <= c + dy[back_d] < m and graph[r + dx[back_d]][c + dy[back_d]] != 1:
            r += dx[back_d]
            c += dy[back_d]
            
        else:
            break


answer = 0
for i in range(n):
    answer += graph[i].count(-1)

print(answer)