def trans_n_nary(n, number):
    s = '0123456789ABCDEF'
    result = ''
    if number == 0:
        return '0'
    while number:
        result = s[number % n] + result
        number //= n
    return result

def solution(n, t, m, p):
    answer = ''
    text = ''
    for i in range(t*m):
        text += trans_n_nary(n, i)
    
    for i in range(p-1, t*m, m):
        answer += text[i]
    return answer