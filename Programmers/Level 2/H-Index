def solution(citations):
    answer = len(citations)
    
    citations.sort(reverse=True)
    while True:
        count = 0
        for i in citations:
            if i >= answer:
                count += 1
        if count >= answer:
            return answer
        else:
            answer -= 1