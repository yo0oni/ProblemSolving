import sys
input = sys.stdin.readline

n = int(input())
time = []
for _ in range(n):
    a, b = map(int, input().split())
    time.append((a, b))

time.sort(key = lambda x: (x[1], x[0]))

count = 1
end_time = time[0][1] # 시작
for index in range(1, len(time)):
    if end_time <= time[index][0]:
        count += 1
        end_time = time[index][1]
    
print(count)