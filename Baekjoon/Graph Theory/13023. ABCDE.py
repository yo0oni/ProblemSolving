import sys
input = sys.stdin.readline


def dfs(index, depth):
    global answer

    visited[index] = True
    if depth == 4:
        answer = True
        return
    for i in friends[index]:
        if not visited[i]:
            dfs(i, depth+1)
            visited[i] = False

n, m = map(int, input().split())
friends = [[] for _ in range(n)]
answer = False
visited = [False]*2001

for i in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if answer:
        break

if answer:
    print(1)
else:
    print(0)