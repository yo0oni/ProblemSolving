import sys
input = sys.stdin.readline

N, L = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(N)]
    
# 접근 : L길이를 기준으로 생각하자
# 주의 : 배열은 0부터 시작하는데 i + j는 N 기준으로 할 수 있음

# 경사로는 낮은 칸과 높은 칸을 연결하며, 아래와 같은 조건을 만족해야한다.

# 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
# 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
# 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.
# 아래와 같은 경우에는 경사로를 놓을 수 없다.

# 경사로를 놓은 곳에 또 경사로를 놓는 경우
# 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
# 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
# 경사로를 놓다가 범위를 벗어나는 경우

answer = 0

def is_ok(line):
    visited = [False for _ in range(N)]
    
    for i in range(N-1):
        if line[i] == line[i+1]:
            continue
        
        if abs(line[i] - line[i+1]) >= 2:
            return False
        
        if line[i] > line[i+1]:
            for j in range(1, L+1):
                if i + j >= N or visited[i + j] or line[i+1] != line[i + j]:
                    return False
                visited[i + j] = True 
        
        
        if line[i] < line[i+1]:
            for j in range(L):
                if i - j < 0 or visited[i - j] or line[i] != line[i - j]:
                    return False
                visited[i - j] = True
        
    return True

# 가로 탐색
for i in range(N):
    if is_ok(lines[i]):
        answer += 1

# 세로 탐색
for j in range(N):
    if is_ok([lines[i][j] for i in range(N)]):
        answer += 1

print(answer)