import sys
from collections import deque
input = sys.stdin.readline

c = int(input())
n = int(input())
answer = 0
computer = [[0] * (c+1) for _ in range(c+1)]
visited = [False] * (c+1)

def bfs(number):
    global computer, answer
    dq = deque([number])
    visited[number] = True
    
    while dq:
        current = dq.popleft()
        
        for index in range(1, c+1):
            if not visited[index] and computer[current][index] == 1:
                visited[index] = True
                dq.append(index)
                answer += 1
                
    return answer
    

for _ in range(n):
    a, b = map(int, input().split())
    computer[a][b] = computer[b][a] = 1

print(bfs(1))