def solution(clothes):
    answer = 1
    clodict = {}
    
    for i in clothes:
        if i[1] in clodict:
            clodict[i[1]] += 1
            continue
            
        clodict[i[1]] = 1
        
    for v in clodict.values():
        answer = (v+1)*answer
        
    return answer - 1