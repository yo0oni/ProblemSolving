import sys
from collections import deque
input = sys.stdin.readline

def can_arrive_festi():
    dq = deque([(home_x, home_y)])
    
    while dq:
        x, y = dq.popleft()
        
        if abs(x - festi_x) + abs(y - festi_y) <= 1000:
            return True
        
        for index in range(n):
            if not visited[index]:
                conven_x, conven_y = convens[index]
                
                if abs(conven_x - x) + abs(conven_y - y) <= 1000:
                    dq.append((conven_x, conven_y))
                    visited[index] = True

    return False

t = int(input())
for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    convens = [list(map(int, input().split())) for _ in range(n)]
    festi_x, festi_y = map(int, input().split())
    visited = [False] * (n+1)
    
    if can_arrive_festi():
        print("happy")
    else:
        print("sad")