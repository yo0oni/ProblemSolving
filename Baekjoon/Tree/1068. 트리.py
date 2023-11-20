import sys
input = sys.stdin.readline

def find_leaf(child):
    global count, visited, delete_node

    if child == delete_node:
        return

    if len(graph[child]) == 0:
        count += 1
        return

    for child in graph[child]:
        if visited[child]:
            continue

        visited[child] = True
        find_leaf(child)


N = int(input())
arr = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
root = -1

for index in range(N):
    parent = arr[index]

    if parent == -1:
        root = index
        continue

    graph[parent].append(index)

delete_node = int(input())
graph[delete_node] = []

for g in graph:
    if delete_node in g:
        g.remove(delete_node)

visited = [False] * N
count = 0

visited[root] = True
find_leaf(root)

print(count)