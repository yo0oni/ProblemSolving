from itertools import permutations

def solution(k, dungeons):
    answer = -1
    perms = list(permutations(dungeons,len(dungeons)))
    
    for perm in perms:
        cnt = 0
        energy = k
        
        for p in perm:
            if energy >= p[0]:
                energy -= p[1]
                cnt += 1
                
        if cnt > answer:
            answer = cnt
            
    return answer