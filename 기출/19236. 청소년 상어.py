import sys, collections
from collections import deque
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

sea = [[[0]*2 for _ in range(4)] for _ in range(4)]
for i in range(4):
    fish_lst = list(map(int, input().split()))
    for j in range(4):
        sea[i][j] = [fish_lst[j*2], fish_lst[j*2+1]-1]

def find_fish(number, sea):
    for i in range(4):
        for j in range(4):
            if sea[i][j][0] == number:
                return i, j, sea[i][j][1]

def dfs(si, sj, sd, total, sea):
    global answer
    answer = max(total, answer)
    
    # 물고기 이동
    for number in range(1, 17):
        ci, cj, dir = find_fish(number, sea)
        
        if dir == -1: # 물고기 없으면
            continue
        
        for d in range(8):
            td = (d + dir) % 8
            ni = dx[td] + ci
            nj = dy[td] + cj
            
            if 0 <= ni < 4 and 0 <= nj < 4 and (ni, nj) != (si, sj):
                sea[ci][cj][1] = td
                sea[ni][nj], sea[ci][cj] = sea[ci][cj], sea[ni][nj]
                break

    for mul in range(1, 4):
        ni, nj = si + dx[sd]*mul, sj + dy[sd]*mul
        
        if 0 <= ni < 4 and 0 <= nj < 4 and sea[ni][nj][1] != -1:
            fn, fd = sea[ni][nj] # 상어가 도착한 곳에 있는 물고기
            sea[ni][nj][1] = -1
            new_sea = [[x[:] for x in row] for row in sea]
            
            dfs(ni, nj, fd, total+fn, new_sea)
            
            sea[ni][nj][1] = fd
            

answer = 0
fn,fd = sea[0][0]       # 물고기 먹는처리 주의(방향 ..[1]=-1)
sea[0][0][1]=-1       # (0,0)위치 물고기 먹기 처리
dfs(0, 0, fd, fn, sea)
print(answer)