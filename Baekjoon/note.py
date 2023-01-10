from collections import deque, defaultdict


def bfs(start, visited):
    if start == K:
        return 0
    q = deque()
    q.append((N, 0))
    visited[N] = True
    
    while q:
        idx, time = q.popleft()
        if idx == K:
            return time
        for pos in [idx*2, idx+1, idx-1]:
            if 0 <= pos <= MAX and not visited[pos]:
                visited[pos] = True
                if pos == idx*2:
                    q.appendleft((pos, time))
                else:
                    q.append((pos, time+1))

N, K = map(int, input().split())
MAX = 100000
visited = [False] * (MAX+1)
print(bfs(N, visited))
