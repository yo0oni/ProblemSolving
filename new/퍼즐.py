import sys
from collections import deque
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(start):
    dq = deque([(start, 0)])
    visited = set()
    visited.add(numbers)
    
    while dq:
        current, count = dq.popleft()
        
        if current == "123456780":
            return count
            
        zero_index = current.index('0')
        ci = zero_index // 3
        cj = zero_index % 3
        
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            
            if 0 <= ni < 3 and 0 <= nj < 3:
                new_board = list(current)
                swap_idx = ni * 3 + nj
                new_board[zero_index], new_board[swap_idx] = new_board[swap_idx], new_board[zero_index]
                
                new_numbers = ''.join(new_board)
                
                if new_numbers not in visited:
                    visited.add(new_numbers)
                    dq.append((new_numbers, count+1))
    
    return -1

board = [list(map(str, input().split())) for _ in range(3)]
numbers = ""
for i in range(3):
    for j in range(3):
        numbers += board[i][j]
        
print(bfs(numbers))