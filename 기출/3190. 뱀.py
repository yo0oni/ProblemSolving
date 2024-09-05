import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0
current = 0
snakes = deque([(0, 0)])

def change_direction(direction, current):
    if direction == "D": 
        return (current + 1) % 4 # 오른쪽
    else:
        return (current - 1) % 4 # 왼쪽
    

def move(time):
    global answer, snakes, current

    while answer < time:
        answer += 1

        nx, ny = snakes[0]
        nx += dx[current]
        ny += dy[current]

        if 0 <= nx < n and 0 <= ny < n:
            if [nx, ny] in snakes:
                return False
            
            snakes.appendleft([nx, ny])
            if board[ny][nx] != -1:
                snakes.pop()

            else:
                board[ny][nx] = 0
            
        else:
            return False

    return True
            

n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = -1


l = int(input())
previous_time = 0

time_direction = []
for _ in range(l):
    time_direction.append(list(map(str, input().split())))

flag = True
for time, direction in time_direction:
    if not move(int(time)):
        flag = False
        break

    current = change_direction(direction, current)

if flag:
    move(float('inf'))
    print(answer)
else:
    print(answer)