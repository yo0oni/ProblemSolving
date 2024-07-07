import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
operand = list(map(int, input().split()))

max_answer = -1e9
min_answer = 1e9

def dfs(depth, add, minus, multi, div, answer):
    global max_answer, min_answer
    if depth == n:
        max_answer = max(answer, max_answer)
        min_answer = min(answer, min_answer)
        return

    if add:
        dfs(depth+1, add-1, minus, multi, div, answer + numbers[depth])

    if minus:
        dfs(depth+1, add, minus-1, multi, div, answer - numbers[depth])

    if multi:
        dfs(depth+1, add, minus, multi-1, div, answer * numbers[depth])

    if div:
        if answer > 0:
            dfs(depth+1, add, minus, multi, div-1, answer // numbers[depth])
        else:
            dfs(depth+1, add, minus, multi, div-1, (abs(answer) // numbers[depth]))

dfs(1, operand[0], operand[1], operand[2], operand[3], numbers[0])
print(max_answer)
print(min_answer)