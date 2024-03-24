import sys
input = sys.stdin.readline

strings = list(input().strip())
diar = {2:["A","B","C"],
        3:["D","E","F"],
        4:["G","H","I"],
        5:["J","K","L"],
        6:["M","N","O"],
        7:["P","Q","R","S"],
        8:["T","U","V"],
        9:["W","X","Y","Z"]}

result = 0
for string in strings:
    for key in diar.keys():
        if string in diar[key]:
            result += (key+1)
    
print(result)