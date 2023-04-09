def solution(N, stages):
    answer = []
    d = dict()
    length = len(stages)
    for i in range(1,N+1): # 1, 2, 3, 4, 5
        if length != 0:
            d[i] = stages.count(i)/length
        else:
            d[i] = length
        length = length - stages.count(i)
    d1 = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for key in d1:
        answer.append(key[0])
    return answer