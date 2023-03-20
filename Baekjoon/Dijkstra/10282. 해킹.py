import sys
import heapq
input = sys.stdin.readline
 
T = int(input())
 
for _ in range(T):
    n, d, start = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    time = [sys.maxsize]*(n+1)
    time[start] = 0
    queue = [[0, start]]
    for _ in range(d):
        a, b, s = map(int, input().split())
        arr[b].append([a, s])
 
    while queue:
        w, s = heapq.heappop(queue)
        for e, v in arr[s]:
            if time[e] > w+v:
                time[e] = w+v
                heapq.heappush(queue, [w+v, e])
 
    _max = 0
    cnt = 0
    for i in time:
        if i != sys.maxsize:
            _max = max(i, _max)
            cnt += 1
 
    print(cnt, _max)