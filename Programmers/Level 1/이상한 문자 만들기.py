def solution(s):
    answer = ''
    strs = s.split(" ")
    count = 0
    for j in strs:
        for i in range(len(j)):
            if i%2 == 0:
                answer += s[count].upper()
            else:
                answer += s[count].lower()
            count += 1
        count += 1
        answer += " "
    return answer[:-1]