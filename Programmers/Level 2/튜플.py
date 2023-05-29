def solution(s):
    answer = []
    
    splitted = s[2:-2].split("},{") 

    splitted2 = sorted([spl.split(',') for spl in splitted], key=lambda x:len(x))

    answer.append(int(splitted2[0][0]))
    for i in range(1, len(splitted2)):
        for s in splitted2[i]:
            if s not in splitted2[i-1]:
                answer.append(int(s))
                break

    return answer