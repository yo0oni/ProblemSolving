import sys
input = sys.stdin.readline

n = int(input())
average = list(map(int, input().split()))
max_avg = max(average)

new = []
for avg in average:
    new.append(avg/max_avg*100)

print(sum(new)/len(new))