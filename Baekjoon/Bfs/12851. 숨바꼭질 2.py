from collections import deque

def bfs():
    count = 0
    queue = deque([n])
    while queue:
        x = queue.popleft()
        # 수빈이와 동생의 위치가 같다면 종료
        if x==k:
            count += 1
            continue
        for i in (x-1, x+1, x*2):
            # 추가된 코드 : 같은 층일때 최단거리가 중복으로 나와도 생략하지 않고 추가해줌
            if 0 <= i <= max_num and (visited[i] == visited[x] + 1 or visited[i] == 0):
                visited[i] = visited[x] + 1
                queue.append(i)
            # elif 0 <= i <= max_num and visited[i]:
            #     redu.append(i)
    print(visited[k])
    print(count)

max_num = 100000
visited = [0] * (max_num+1)
n, k = map(int, input().split())
bfs()