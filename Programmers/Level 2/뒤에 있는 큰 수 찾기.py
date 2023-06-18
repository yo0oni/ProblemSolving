from collections import deque

def solution(maps):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    r = len(maps)
    c = len(maps[0])

    graph = [[-1]*c for _ in range(r)]
    
    queue = deque()
    queue.append([0, 0])

    graph[0][0] = 1 # 여기서 시작하니까 시작과 동시에 방문

    while queue:
        y, x = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1 # 갱신하면서 거리 더하기
                    queue.append([ny, nx])

    answer = graph[-1][-1]
    return answer