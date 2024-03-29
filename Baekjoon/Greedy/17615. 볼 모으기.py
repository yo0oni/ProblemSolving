import sys
input = sys.stdin.readline

n = int(input())
balls = input().strip()
count = []

rexplore = balls.rstrip('R')
count.append(rexplore.count('R'))

rexplore = balls.rstrip('B')
count.append(rexplore.count('B'))

lexplore = balls.lstrip('R')
count.append(lexplore.count('R'))

lexplore = balls.lstrip('B')
count.append(lexplore.count('B'))

print(min(count))