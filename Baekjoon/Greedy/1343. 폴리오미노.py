import sys
input = sys.stdin.readline

board = input().replace("XXXX", "AAAA").replace("XX", "BB")

if 'X' in board:
    print(-1)
    
else:
    print(board)