import datetime

def solution(today, terms, privacies):
    answer = []
    term = {}
    
    year, month, day = map(int, today.split('.'))
    today = datetime.datetime(year, month, day)
    
    for t in terms:
        a, b = map(str, t.split())
        term[a] = int(b)
    
    number = 0
    for p in privacies:
        date, term_type = map(str, p.split())
        year, month, day = map(int, date.split('.'))
        month += term[term_type]
        day -= 1
        
        if day == 0:
            month -= 1
            day = 28
        
        if month % 12 == 0: 
            year += (month // 12) - 1
            month = 12
            
        else:
            year += month // 12
            month = month % 12
        
        check = datetime.datetime(year, month, day)
        
        if check < today:
            answer.append(number+1)
        number += 1
    
    return answer
