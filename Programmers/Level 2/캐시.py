from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    if cacheSize == 0:
        return len(cities)*5
    
    for i in cities:
        i = i.upper() 
        
        if i in cache:
            answer += 1
            cache.remove(i)
            cache.appendleft(i)
            
        else:
            if len(cache) == cacheSize and cacheSize :
                cache.pop()
                
            answer += 5
            cache.appendleft(i)
        
    return answer