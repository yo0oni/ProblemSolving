import sys
import heapq

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
for _ in range(n):
    # 도로 건설 비용 및 도로 건설 금지 구역 입력받음
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def Dijkstra():
    distances = [[INF for _ in range(m)] for _ in range(n)]
    # 0,0 초기화
    distances[0][0] = graph[0][0]
    q = []
    if distances[0][0] == -1: # 0,0이 -1이면 시작 불가능
        return INF
    else:
        # 1, 0, 0
        heapq.heappush(q, [distances[0][0], 0, 0])

    while q:
        print(q)
        cur_cost, cur_row, cur_col = heapq.heappop(q)
        print(cur_cost)

        if distances[cur_row][cur_col] < cur_cost: # 1, 1
            continue

        for x, y in zip(dx, dy):
            next_row, next_col = cur_row + y, cur_col + x
            # print(next_row, next_col)
            # 범위 체크
            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m:
                continue
            
            # 체크할 도로의 건설 비용 체크
            next_cost = graph[next_row][next_col]

            # -1이 아니고 더 저렴하면 진행
            if distances[next_row][next_col] > cur_cost + next_cost and next_cost != -1:
                # 현재까지의 건설 비용과 해당 도로의 건설 비용을 더해가며 반복문 진행
                distances[next_row][next_col] = cur_cost + next_cost
                heapq.heappush(q, [cur_cost + next_cost, next_row, next_col])

    return distances[n-1][m-1]

answer = Dijkstra()
if answer == INF:
    print(-1)
else:
    print(answer)