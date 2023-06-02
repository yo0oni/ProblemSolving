from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque(priorities)
    
    while dq:
        max_priorty = max(dq)
        priorty = dq.popleft()
        location -= 1
        
        if priorty < max_priorty:
            dq.append(priorty)
            if location < 0:
                location = len(dq) - 1
                
        else:
            answer += 1
            if location < 0:
                break
            
    return answer