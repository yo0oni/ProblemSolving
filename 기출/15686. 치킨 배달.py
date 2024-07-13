import sys
from itertools import combinations
from collections import defaultdict
input = sys.stdin.readline

def calculate_distance(chickens):
    total_distance = 0

    for house in houses:
        min_distance = 1e9

        for chicken in chickens:
            chicken_x, chicken_y = chicken[0], chicken[1]
            house_x, house_y = house[0], house[1]
            distance = abs(chicken_x - house_x) + abs(chicken_y - house_y)
            
            if min_distance > distance:
                min_distance = distance

        total_distance += min_distance
    return total_distance


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
houses = []
chicken_houses = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append([i+1, j+1])

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken_houses.append([i+1, j+1])

min_distance = 1e9
for chickens in combinations(chicken_houses, m):
    distance = calculate_distance(chickens)
    if min_distance > distance:
        min_distance = distance
print(min_distance)