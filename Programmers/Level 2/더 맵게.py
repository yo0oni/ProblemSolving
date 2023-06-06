from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while scoville[0] < K:
        
        if len(scoville) <= 2 and (scoville[0]+scoville[1]*2) < K:
            return -1
        
        heappush(scoville, heappop(scoville)+(heappop(scoville)*2))
        answer += 1
        
    return answer