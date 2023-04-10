from itertools import combinations

def solution(numbers):
    answer = []
    combi = list(combinations(numbers, 2))
    for i in combi:
        print(i)
        if i[0] + i[1] not in answer:
            answer.append(i[0] + i[1])
        else:
            continue
    answer.sort()
    return answer