import sys, collections
from collections import deque
from itertools import combinations

def bfs(numbers):    
    dq = deque()
    dq.append(numbers[0])
    visited = set([numbers[0]])
    total = 0
    
    while dq:
        current = dq.popleft()
        total += people[current]
        
        for number in numbers:
            if number in connect[current] and number not in visited:
                visited.add(number)
                dq.append(number)
    
    return total, len(visited)


n = int(input())
people = list(map(int, input().split()))
connect = collections.defaultdict(list)
answer = float('inf')
cities = [i for i in range(n)]
count = 0

for index in range(n):
    inputs = list(map(int, input().split()))
    connect[index] = [x-1 for x in inputs[1:]]


for i in range(1, n//2 + 1):
    for combi in combinations(cities, i):
        first_people, first_visited = bfs(list(combi))
        second_people, second_visited = bfs([i for i in range(n) if i not in combi])
        
        if first_visited + second_visited == n:
            answer = min(answer, abs(first_people - second_people))

if answer == float('inf'):
    print(-1)
else:
    print(answer)