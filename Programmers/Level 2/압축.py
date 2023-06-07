def solution(msg):
    answer = []
    eng = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    while len(msg) > 0:
        w = msg[0]
        cnt = 0
        if len(msg) == 1:
            answer.append(eng.index(w)+1)
            break

        while len(w) < len(msg):
            s = w
            cnt += 1
            w += msg[cnt]
            if w not in eng:
                w = s
                break

        answer.append(eng.index(w)+1)
        msg = msg[len(w):]

        if msg:
            eng.append(w + msg[0])
            
    return answer