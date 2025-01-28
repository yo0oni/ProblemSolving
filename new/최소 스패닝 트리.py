import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    parent_x = find_parent(x)
    parent_y = find_parent(y)

    if parent_x < parent_y:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y

v, e = map(int, input().split())
costs = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    costs.append((cost, a, b))

costs.sort()
parent = [0] * (v+1)
total_cost = 0

for i in range(1, v+1):
    parent[i] = i

print(parent)
for i in range(e):
    cost, a, b = costs[i]
    
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        total_cost += cost

print(total_cost)