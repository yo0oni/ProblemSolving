def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for j in range(len(board[1])):
            if board[j][i-1] != 0:
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2
    return answer
