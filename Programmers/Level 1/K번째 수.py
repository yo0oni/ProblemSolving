def solution(array, commands):
    answer = []
    for i in commands:
        sort = sorted(array[(i[0]-1):i[1]])
        answer.append(sort[i[2]-1])
        
    return answer