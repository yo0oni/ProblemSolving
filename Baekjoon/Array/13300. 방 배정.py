import sys, math
input = sys.stdin.readline

n, k = map(int, input().split())
girl = dict()
boy = dict()

for i in range(1, 7):
    girl[i] = 0
    boy[i] = 0

for _ in range(n):
    gender, grade = map(int, input().split())

    if gender == 0:
        girl[grade] += 1
    
    else:
        boy[grade] += 1

def count_room(gender):
    count = 0

    for i in range(1, 7):
        if gender[i] > k:
            count += math.ceil(gender[i] / k)
        elif gender[i] == 0:
            continue
        else:
            count += 1

    return count

print(count_room(girl) + count_room(boy))