import sys
from collections import deque
input = sys.stdin.readline

def bfs(weight):
	queue = deque()
	queue.append(factory_1)
	visited = [False] * (n+1)
	visited[factory_1] = True
	
	while queue:
		x = queue.popleft()
		
		for i, w in bridge[x]:
			if not visited[i] and w >= weight: # 최대 중량을 가져갈 수 있어야함
				visited[i] = True
				queue.append(i)
	
	if visited[factory_2]:
		return True
	else:
		return False
	

n, m = map(int, input().split())
bridge = [[] for _ in range(n+1)]

for i in range(m):
	a, b, c = map(int,input().split())
	bridge[a].append([b,c])
	bridge[b].append([a,c])
	
factory_1, factory_2 = map(int,input().split())

start = 1
end = 1000000000

result = 0
while start <= end:
	mid = (start + end) // 2
	
	if bfs(mid):
		result = mid
		start = mid + 1
	else:
		end = mid - 1
		
print(result)