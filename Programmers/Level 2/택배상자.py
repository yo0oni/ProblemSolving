def solution(order):
    answer = 0
    sub = []
    box = 1
    
    while box != len(order)+1:
        sub.append(box)
        
        while sub[-1] == order[answer]:
            answer += 1
            sub.pop()
            if len(sub) == 0:
                break
                
        box += 1
        
    return answer