import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n = int(input())
seat = [[0]*n for _ in range(n)]
profer = dict()
result = 0
 
for _ in range(n*n):
    list_ = list(map(int, input().split()))
    profer[list_[0]] = list_[1:]
    
    max_x = 0
    max_y = 0
    max_like = -1
    max_empty = -1
    for i in range(n):
        for j in range(n):
            if seat[i][j] == 0:
                like_count = 0
                empty_count = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if seat[nx][ny] in list_:
                            like_count += 1
                        if seat[nx][ny] == 0:
                            empty_count += 1
                            
                if max_like < like_count or (max_like == like_count and max_empty < empty_count):
                    max_x = i
                    max_y = j
                    max_like = like_count
                    max_empty = empty_count
                    
    seat[max_x][max_y] = list_[0]
    
for i in range(n):
    for j in range(n):
        count = 0
        like = profer[seat[i][j]]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                # print(seat[i][j],seat[nx][ny], like)
                if seat[nx][ny] in like:
                    count += 1
        if count != 0:
            result += 10 ** (count-1)
            
print(result)