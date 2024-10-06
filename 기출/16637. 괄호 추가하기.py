import sys
input = sys.stdin.readline

def calculate(a, b, op):
    if op == "+":
        return a + b
    
    elif op == "-":
        return a - b
    
    else:
        return a * b
    

def dfs(index, current_value):
    global max_answer
    if index >= n:
        max_answer = max(max_answer, current_value)
        return
    
    # 괄호 없이 풀리는 경우
    next_value = calculate(current_value, int(expression[index+1]), expression[index])
    dfs(index+2, next_value)
    
    # 괄호 있어야 풀리는 경우
    if index + 4 <= n:
        bracket_value = calculate(int(expression[index+1]), int(expression[index+3]), expression[index+2])
        next_value = calculate(current_value, bracket_value, expression[index])
        dfs(index+4, next_value)
        
    return max_answer

n = int(input())
expression = list(input().strip())
max_answer = float('-inf')

if len(expression) == 1:
    print(expression[0])
else:
    print(dfs(1, int(expression[0])))