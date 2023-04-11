def solution(n):
    answer = ''
    while n > 0:
        n,r = divmod(n,3)
        answer += str(r)
        print(answer)
    return int(answer, 3)