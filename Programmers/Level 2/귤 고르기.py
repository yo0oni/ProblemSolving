def solution(k, tangerine):
    answer = 0
    dicts = {}
    for i in tangerine:
        if i in dicts:
            dicts[i]+=1
        else:
            dicts[i]=1
    dicts = dict(sorted(dicts.items(), key=lambda x: x[1], reverse=True))
    
    for i in dicts:
        if k<=0:
            return answer
        k -= dicts[i]
        answer+=1
        
    return answer
