import math

def solution(n, words):
    answer = []
    stack = []
    start = end = list(words[0])[0]
    
    num = turn = 0
    
    for word in words:
        turn += 1
        num = num%n
        start = list(word)[0]
        
        if word in stack or start != end:
            return [num+1, math.ceil(turn/n)]
        
        else:
            stack.append(word)
            
        num += 1
        end = list(word)[-1]
        
    return [0, 0]