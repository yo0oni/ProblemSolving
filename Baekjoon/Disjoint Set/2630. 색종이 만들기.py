import sys

n = int(input())
paper = []
white = blue = 0
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

def check(x, y, n):
    global white, blue
    color = paper[x][y]
    for i in range(x, x+n): # 0 8
        for j in range(y, y+n): # 0 8
            if color != paper[i][j]:
                check(x, y, n//2) # 0 0 4
                check(x + n//2, y, n//2) # 4 0 4
                check(x, y + n//2, n//2) # 0 4 4
                check(x + n//2, y + n//2, n//2) # 4 4 4
                return
    
    if color == 0:
        white += 1
    else:
        blue += 1

check(0,0,n)
print(white, blue, sep='\n')