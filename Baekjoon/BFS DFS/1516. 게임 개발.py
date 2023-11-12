import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
time = []
count = [0] * (n+1)
pre_construct = [[0] for _ in range(n+1)]

for i in range(1, n+1):
    arr = list(map(int, input().split()))
    time.append(arr[0])
    for pre in arr[1:-1]:
        pre_construct[pre].append(i)
        count[pre] += 1

result = [0] * (n+1)
dq = deque()

for i in range(1, n+1):
    if count[i] == 0: # 선건설 건물이 없으면 한번에 끝
        dq.append(i)
        result[i] = time[i]

while dq:
    now = dq.popleft()
    for i in pre_construct[now]:
        count[now] -= 1
        result[now] = max(result[now] + time[i], result[i])

        if count[i] == 0:
            dq.append(i)

print()