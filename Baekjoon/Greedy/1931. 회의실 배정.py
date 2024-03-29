import sys
input = sys.stdin.readline

n = int(input())
times = []
for _ in range(n):
    a, b = map(int, input().split())
    times.append((a, b, b-a))
times.sort(key=lambda x:(x[1], x[0], x[2]))

count = 1
start = times[0][1]
for index in range(len(times)-1):
    if start <= times[index+1][0]:
        start = times[index+1][1]
        count += 1

print(count)