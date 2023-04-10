def solution(food):
    answer = ''
    left = ''
    right = ''
    for i in range(1, len(food)):
        while food[i] > 1:
            right = right + str(i)
            left = str(i) + left
            food[i] = food[i] - 2
    answer = right + '0' + left
    return answer