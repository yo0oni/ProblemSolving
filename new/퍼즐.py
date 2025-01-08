import sys
from collections import deque
input = sys.stdin.readline

board = [list(map(str, input().split())) for _ in range(3)]
# 0의 위치를 저장해야댐
# 그러고 상하좌우에 있는 숫자들 이동
numbers = ""
for i in range(3):
    for j in range(3):
        numbers += board[i][j]

dq = deque([(numbers, 0)])
visited = set()
visited.add(numbers)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

while dq:
    current, count = dq.popleft()
    
    if current == "123456780":
        print(count)
        sys.exit(0)
    
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
            
print(-1)