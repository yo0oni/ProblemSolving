import sys
input = sys.stdin.readline

n, d = map(int, input().split())
highways = []
for _ in range(n):
    start, end, short = map(int, input().split())
    highways.append([start, end, short])

distance = [i for i in range(d+1)]

for i in range(d + 1):
    distance[i] = min(distance[i], distance[i - 1] + 1)
    
    for start, end, short in highways:
        if i == start and end <= d and short < distance[end] - distance[i]:
            distance[end] = distance[i] + short
    
print(distance[d])