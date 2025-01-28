import sys
from collections import deque
input = sys.stdin.readline


def bfs(si):
    tree = [si]
    dq = deque([si])
    visited[si] = True

    while dq:
        ci = dq.popleft()

        for ni in friend[ci]:
            if not visited[ni]:
                visited[ni] = True
                dq.append(ni)
                tree.append(ni)

    return tree


n, m, k = map(int, input().split())
prices = [0] + list(map(int, input().split()))
friend = [[] for _ in range(n+1)]
for _ in range(m):
    v, w = map(int, input().split())
    friend[w].append(v)
    friend[v].append(w)
visited = [False for _ in range(n+1)]

tree = []
# 먼저 트리를 구하고
for i in range(1, n+1):
    if not visited[i]:
        tree.append(bfs(i))

total_price = 0
for friends in tree:
    min_price = float('inf')

    for friend in friends:
        if min_price > prices[friend]:
            min_price = prices[friend]
    
    total_price += min_price

if total_price > k:
    print("Oh no")
else:
    print(total_price)

# 거기서 최솟값인 애들끼리 더하기
# 그게 만약 예산을 넘으면 oh no