import sys
input = sys.stdin.readline


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    parent_x = find_parent(x)
    parent_y = find_parent(y)

    if parent_x > parent_y:
        parent[parent_x] = parent_y
    else:
        parent[parent_y] = parent_x


n = int(input())
m = int(input())
costs = []
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    costs.append((cost, a, b))

costs.sort()
total_cost = 0
for i in range(m):
    cost, a, b = costs[i]

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        total_cost += cost

print(total_cost)