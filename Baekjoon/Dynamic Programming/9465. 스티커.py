import sys
input = sys.stdin.readline

def find_max(n, stickers):
    d = [[0] * n for _ in range(2)]

    d[0][0] = stickers[0][0]
    d[1][0] = stickers[1][0]
    if n == 1:
        return max(d[0][0], d[1][0])
    
    d[0][1] = stickers[1][0]+stickers[0][1]
    d[1][1] = stickers[0][0]+stickers[1][1]
    if n == 2:
        return max(d[0][1], d[1][1])

    for i in range(2, n):
        d[0][i] = max(d[1][i - 2], d[1][i - 1]) + stickers[0][i]         
        d[1][i] = max(d[0][i - 2], d[0][i - 1]) + stickers[1][i]
    
    return max(d[0][-1], d[1][-1])


t = int(input())

for _ in range(t):
    n = int(input())
    stickers = []

    for _ in range(2):
        stickers.append(list(map(int, input().split())))

    print(find_max(n, stickers))