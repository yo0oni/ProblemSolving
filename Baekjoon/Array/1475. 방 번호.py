import sys
input = sys.stdin.readline

numbers = input().strip()
count = [0] * 10

for number in numbers:
    if number == '9' or number == '6':
        if count[9] < count[6]:
            count[9] += 1
        else:
            count[6] += 1
    else:
        count[int(number)] += 1
        
print(max(count))