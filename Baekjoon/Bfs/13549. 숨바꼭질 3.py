from collections import deque

def bfs():
    queue = deque()
    queue.append((n,0))
    visited[n] = True
    while queue:
        x, time = queue.popleft()
        if x==k:
            print(time)
            break
        for i in (x*2, x+1, x-1):
            if 0 <= i <= max_num and not visited[i]:
                visited[i] = True
                if i == x*2:
                    queue.appendleft((i, time))
                else:
                    queue.append((i, time+1))

max_num = 1000000
visited = [False] * (max_num+1)
n, k = map(int, input().split())
bfs()