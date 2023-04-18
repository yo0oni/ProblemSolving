import numpy

def solution(keymap, targets):
    answer = []
    
    for target in targets:
        count = 0
        
        for t in target:
            idx_list = []
            
            for key in keymap:
                try:
                    idx_list.append(key.index(t))
                    
                except:
                    idx_list.append(numpy.inf)
                    
            count += (min(idx_list) + 1)
        
        if count == numpy.inf:
            answer.append(-1)
        
        else:
            answer.append(count)
            
    return answer