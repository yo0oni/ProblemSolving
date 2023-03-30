import sys
input = sys.stdin.readline

n = int(input())
meeting = []
for i in range(n):
    start, end = map(int, input().split())
    meeting.append([start,end])
meeting.sort(key = lambda x: (x[1], x[0]))

count = 1
end_time = meeting[0][1] # 4
for i in range(1, n): # 일단 마지막 회의까지 다 세줌
    if meeting[i][0] >= end_time: # 시작 시간이 앞 회의 끝나는 시간보다 늦으면 ok
        count += 1
        end_time = meeting[i][1]

print(count)