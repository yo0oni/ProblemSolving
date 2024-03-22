import sys
input = sys.stdin.readline

n = int(input())
students = [list(map(int, input().split())) for _ in range(n*n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

seat = [[0] * n for _ in range(n)]
for student in students:
    seat_info = []

    for x in range(n):
        for y in range(n):
            if seat[x][y] == 0:
                like, empty = 0, 0

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < n and 0 <= ny < n:
                        if seat[nx][ny] in student[1:]:
                            like += 1

                        if seat[nx][ny] == 0:
                            empty += 1
                        
                seat_info.append((x, y, like, empty))
    
    seat_info.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    seat[seat_info[0][0]][seat_info[0][1]] = student[0]

answer = 0
score = [0, 1, 10, 100, 1000]
students.sort()

for x in range(n):
    for y in range(n):
        count = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if seat[nx][ny] in students[seat[x][y]-1]:
                    count += 1

        answer += score[count]
        
print(answer)