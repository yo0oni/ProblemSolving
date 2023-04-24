def solution(s):
    count = zero_count = 0
    
    while s != '1':
        count += 1
        zero_count += s.count('0')
        s = bin(len(s.replace('0','')))[2:]
        
    return [count, zero_count]