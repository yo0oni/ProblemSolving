from collections import deque
import math

def solution(progresses, speeds):
    dq = deque()
    answer = []
    count = 1

    for i in range(len(speeds)):
        dq.append(math.ceil((100-progresses[i])/float(speeds[i])))
    dq.reverse(); start = dq.pop()

    while dq:
        next = dq.pop()
        if start >= next:
            count += 1
        else:
            answer.append(count)
            start = next
            count = 1

    answer.append(count)
    return answer