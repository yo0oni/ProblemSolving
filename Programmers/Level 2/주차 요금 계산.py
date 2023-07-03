from datetime import datetime
from math import ceil

def solution(fees, records):
    dic = {}; time = {}; answer = []
    base, base_fee, min, min_fee  = fees[0], fees[1], fees[2], fees[3]
    
    for i in records:
        time[i.split()[1]] = 0
    
    for i in records:
        i = i.split()
        
        if i[2]=="IN" and i[1] not in dic:
            dic[i[1]] = i[0]
           
        elif i[2] == "OUT" and i[1] in dic:
            past = datetime.strptime(dic[i[1]], "%H:%M")
            now =  datetime.strptime(i[0], "%H:%M")
            time[i[1]] += ((now-past).seconds // 60)
            dic.pop(i[1])
    
    if dic:
        for i in dic.items():
            last = datetime.strptime("23:59", "%H:%M")
            past = datetime.strptime(i[1], "%H:%M")
            time[i[0]] += (last-past).seconds // 60
            
    stime = sorted(time.items())
    
    for t in stime:
        if t[1] > base:
            answer.append(base_fee + ceil((t[1] - base) / min) * min_fee)
        else:
            answer.append(base_fee)
            
    return answer