import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board=[]
for i in range(n):
    board.append(input())
    
count = []
for a in range(n-7):
    for b in range(m -7):
        w_count = 0
        b_count = 0
        
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        w_count += 1
                    else:
                        b_count += 1
                else:
                    if board[i][j] != 'W':
                        b_count += 1
                    else:
                        w_count += 1
                        
        count.append(w_count)
        count.append(b_count)

print(min(count))
