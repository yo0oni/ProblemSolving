# 맥주 한 박스에는 맥주가 20개
# 50미터에 한 병씩
# 편의점에 들렸을 때, 빈 병은 버리고 새 맥주 병
# 편의점을 나선 직후에도 50미터를 가기 전에 맥주 한 병을 마셔야 한다.
from collections import deque


def bfs(si, sj, fi, fj):
    global convens
    dq = deque([(si, sj)])
    visited = [False] * 100000
    
    while dq:
        si, sj = dq.popleft()
        
        if abs(si - fi) + abs(sj - fj) <= 1000:
            return "happy"
                
        for index, ci, cj in convens:
            if abs(si - ci) + abs(sj - cj) <= 1000 and not visited[index]:
                visited[index] = True
                dq.append((ci, cj))
                
    return "sad"        
            
            
t = int(input())
for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    convens = deque()
    
    for index in range(n):
        x, y = map(int, input().split())
        convens.append((index, x, y))
    
    festival_x, festival_y = map(int, input().split())
    
    print(bfs(home_x, home_y, festival_x, festival_y))