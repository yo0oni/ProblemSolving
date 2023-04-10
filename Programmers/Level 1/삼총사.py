from itertools import combinations

def solution(number):
    answer = 0
    l = list(combinations(number, 3))
    for i in l:
        if sum(i) == 0:
            answer += 1
    return answer