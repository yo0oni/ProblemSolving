from itertools import combinations

def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    for i in range(len(combi)):
        for j in range(2, sum(combi[i])):
            
            if (sum(combi[i]))%j == 0:
                break
        else:
            answer += 1
    return answer