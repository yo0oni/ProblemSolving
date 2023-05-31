def solution(s):
    answer = []
    strings = sorted([s.split(',') for s in s[2:-2].split('},{')], key=len)
    for string in strings:
        for s in string:
            if int(s) not in answer:
                answer.append(int(s))
                break
    return answer