from collections import deque

# todo
# 먹을 수 있는 물고기 찾기 (경로 길이 - x - y 정렬)
# 먹을 수 있는 물고기로 가는 경로 확인하기
# 물고기 먹고 위치 갱신하기
# 크기 업그레이드 체크하기

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 먹을 수 있는 물고기 탐색
def bfs(baby_x, baby_y, baby_size):
    fishes = []
    
    dq = deque()
    dq.append((baby_x, baby_y))
    visited = [[False] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    
    while dq:
        x, y = dq.popleft()
        
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if sea[nx][ny] == 0 or sea[nx][ny] == baby_size: # 헤임칠 수 있으면
                    distance[nx][ny] = distance[x][y] + 1
                    visited[nx][ny] = True
                
                elif 0 < sea[nx][ny] < baby_size: # 먹을 수 있는 물고기가 있으면
                    distance[nx][ny] = distance[x][y] + 1
                    visited[nx][ny] = True
                    fishes.append((distance[nx][ny], nx, ny))
                
                else: # 아기상어보다 큰 물고기들이 있으면 못 지나감
                    visited[nx][ny] = True
                    continue
                    
                dq.append((nx, ny))
    
    fishes.sort()
    return fishes

def resize(count):
    if baby_size == count:
        return True
    return False
         
    
n = int(input())
sea = []
baby_x, baby_y = 0, 0
for index in range(n):
    line = list(map(int, input().split()))
    sea.append(line)
    
    if 9 in line:
        baby_x, baby_y = index, line.index(9)

fishes = []
baby_size = 2
time, count = 0, 0
sea[baby_x][baby_y] = 0

while True:
    can_eat_fishes = bfs(baby_x, baby_y, baby_size)
    
    if not can_eat_fishes:
        break
    
    time += can_eat_fishes[0][0]
    x, y = can_eat_fishes[0][1], can_eat_fishes[0][2]
    sea[x][y] = 0
    baby_x, baby_y = x, y
    count += 1
    
    if resize(count):
        baby_size += 1
        count = 0

print(time)