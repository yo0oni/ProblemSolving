import sys
input = sys.stdin.readline

size = int(input())
answer = 0
board = [0 for i in range(size)]

def Queen(count):
    global answer

    if count == size:
        answer += 1
        return 
    else:
        for x in range(size):
            board[count] = x
            for y in range(count):
                if board[y] == x or abs((x-board[y])/(count-y)) == 1:
                    break
            else: Queen(count+1)

    return answer

print(Queen(0))