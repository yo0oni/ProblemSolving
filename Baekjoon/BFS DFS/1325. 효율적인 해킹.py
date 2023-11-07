import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[b].append(a)

def bfs(i):
    count = 0
    dq = deque([i])
    visited = [False] * (N+1)
    visited[i] = True 
    while dq:
        now = dq.popleft()
        for j in arr[now]:
            if not visited[j]:
                dq.append(j)
                count += 1
                visited[j] = True
    
    return count

result = []
max_cnt = 1
for i in range(1, N + 1):
	cnt = bfs(i)
	if cnt > max_cnt:
		max_cnt = cnt
		result = []
		result.append(i)
	elif cnt == max_cnt:
		result.append(i)

print(*result)