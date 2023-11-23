import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, A, B):
    A = find_parent(parent, A)
    B = find_parent(parent, B)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B

V, E = map(int, input().split())
parent = [0] * (V+1)
for index in range(1, V+1):
    parent[index] = index

tree = []
for _ in range(E):
    A, B, C = map(int, input().split())
    tree.append((C, A, B))

tree.sort()
result = 0
for index in range(E):
    C, A, B = tree[index]

    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        result += C

print(result)