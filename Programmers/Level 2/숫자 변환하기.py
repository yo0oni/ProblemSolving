from collections import deque

def solution(x, y, n):
    visited = [0] * (y + 1)
    queue = deque([x])
    
    while queue:
        tmp = queue.popleft()
        if tmp == y:
            return visited[tmp]
        
        for num in [tmp + n, tmp * 2, tmp * 3]:
            if num <= y and not visited[num]:
                queue.append(num)
                visited[num] = visited[tmp] + 1
    
    return -1