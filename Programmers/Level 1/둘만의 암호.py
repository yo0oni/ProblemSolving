def solution(s, skip, index):
    answer = ''
    character = []
    
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) in skip:
            continue
        character.append(chr(i))
    
    for i in range(len(s)):
        answer += character[(character.index(s[i]) + index) % (len(character))]
    
    return answer