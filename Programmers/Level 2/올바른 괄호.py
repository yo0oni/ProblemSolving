def solution(s):
    stack = []
    
    for i in s:
        if i == ')' and len(stack) >= 1:
            stack.pop()
            continue
        
        stack.append(i)
        
    if len(stack):
        return False

    return True