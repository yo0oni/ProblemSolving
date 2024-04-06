import sys
from itertools import permutations
input = sys.stdin.readline

numbers = []
for number in permutations([1,2,3,4,5,6,7,8,9], 3):
    numbers.append(number)

n = int(input())
for _ in range(n):
    input_number, input_strike, input_ball = map(int, input().split())
    possible = []

    for number in numbers:
        strike, ball = 0, 0

        for index, check_number in enumerate(str(input_number)):
            if int(check_number) == number[index]:
                strike += 1
            if int(check_number) != number[index] and int(check_number) in number:
                ball += 1

        if strike == input_strike and ball == input_ball:
            possible.append(number)

    numbers = possible
    
print(len(possible))