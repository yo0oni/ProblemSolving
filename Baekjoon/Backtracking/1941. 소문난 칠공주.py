from collections import deque

# 조건 1. 7개 조합 중 S의 개수가 4개 이상인지
# 조건 2. 7개들이 붙어있는지 !
# 두 조건이 만족되면 count 증가
# 최종적 count 출력

# bfs로 7명의 여학생이 붙어있는지 확인한다.
def bfs(arr):
    dr = [-1, +1, 0, 0]
    dc = [0, 0, -1, +1]

    # 7명 여학생 위치 방문처리를 위한 리스트 1로 처리
    visited = [[1] * 5 for _ in range(5)]

    # 7명의 여학생 위치를 0으로 초기화
    for i in arr:
        visited[i[0]][i[1]] = 0
    # 첫번째 여학생의 위치를 큐에 넣는다.
    queue = deque([(arr[0])])
    # 첫번째 여학생의 방문처리를 1로 변경
    visited[arr[0][0]][arr[0][1]] = 1
    check = 1  # 여학생들의 위치 방문 횟수(첫 위치 방문했기 때문에 1)
    while queue:
        r, c = queue.popleft()  # 큐에 있는 위치 꺼내기

        for i in range(4):  # 델타 위치를 이동하면서
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위를 벗어나면 진행x
            if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
                continue
            # 만약 위치를 이동하다 아직 여학생 위치를 방문안했다면
            if not visited[nr][nc]:
                visited[nr][nc] = 1  # 그위치를 1로 바꿔주고
                check += 1  # 방문 횟수를 1 증가
                queue.append((nr, nc))  # 큐에 추가
    if check != 7:  # 7번 다 방문하지 않았다면
        return False
    else:  # 7번 방문했다면
        return True

def dfs(depth, start, count):
    global result

    # 조건1을 만족 못하는지 확인
    if count >= 4:  # 만약 임도연파가 4명이상이라면 조건1을 만족하지 못함
        return  # 재귀 탈출

    # 조건2를 만족하는지 확인
    if depth == 7:  # 7명을 뽑았다면 (다솜파는 무조건 4명이상임. 왜냐하면 첫번째 조건문에서 걸러짐)
        if bfs(arr):  # 모든 여학생들이 붙어있다면 조건2까지 만족
            # print(arr)
            result += 1  # 가능한 경우의 수 1개 추가
        return

    for i in range(start, 25): # 1차원으로 늘려놓음 일단
        # r = 0, 0, 0, 0, 0, 1,1, 1 ...
        # c = 0, 1, 2, 3, 4, 0, 1, 2, 3...
        r = i // 5
        c = i % 5
        arr.append((r, c))  # 해당 위치를 추가
        dfs(depth + 1, i + 1, count + (students[r][c] == 'Y'))  # 재귀 돈다.
        arr.pop()  # 해당 위치를 제거


students = [list(input()) for _ in range(5)]
arr = []
result = 0
dfs(0, 0, 0)

print(result)