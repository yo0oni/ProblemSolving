import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def init_doors():
    for key in keys:
        if key == '0':
            break
        doors[ord(key)-97] = True

# 열 수 있는 문은 빈공간으로 변경 -> 어차피 넘어갈 수 있으니까
def init_building():
    for i in range(1, h+1):
        for j in range(1, w+1):
            if building[i][j].isupper() and doors[ord(building[i][j].lower())-97]:
                building[i][j] = '.'

def bfs():
    result = 0
    visited = [[False] * w for _ in range(h)]
    dq = deque()
    dq.append((0, 0)) # 외곽 늘려놨기 때문에 0, 0에서 시작해도 됨
    visited[0][0] = True

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and building[nx][ny] != '*' and not visited[nx][ny]:
                if building[nx][ny] == '.':
                    visited[nx][ny] = True
                    dq.append((nx, ny))

                else:
                    if building[nx][ny] == '$':
                        result += 1
                        visited[nx][ny] = True
                        dq.append((nx, ny))
                        building[nx][ny] = '.'

                    else:
                        if building[nx][ny].isupper(): # 문이 있고
                            if doors[ord(building[nx][ny].lower())-97]: # 문을 열 수 있으면
                                building[nx][ny] = '.'
                                visited[nx][ny] = True
                                dq.append((nx, ny))

                        elif building[nx][ny].islower(): # 열쇠가 있으면
                            doors[ord(building[nx][ny].lower())-97] = True
                            building[nx][ny] = '.'
                            visited = [[False] * w for _ in range(h)]
                            dq = deque()
                            dq.append((nx, ny))

    return result


t = int(input())

for _ in range(t):
    building = []
    h, w = map(int, input().split())

    building.append(['.'] * (w + 2))
    for _ in range(h):
        building.append(['.'] + list(input().strip()) + ['.'])
    building.append(['.'] * (w + 2))

    keys = list(input().strip())
    doors = [False] * 26 # 문 알파벳 26개
    init_doors()
    init_building()

    h, w = h+2, w+2 # 늘린 외곽만큼 증가
    
    print(bfs())