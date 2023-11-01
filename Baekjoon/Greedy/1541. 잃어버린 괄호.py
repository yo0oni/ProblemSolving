import sys
input = sys.stdin.readline

numbers = input().strip().split("-")
minus_numbers = []

for number in numbers:
    if "+" not in number:
        minus_numbers.append(int(number))
    else:
        split_by_plus = map(int, number.split("+"))
        minus_numbers.append(sum(split_by_plus))

result = minus_numbers[0]
for index in range(1, len(minus_numbers)):
    result -= minus_numbers[index]

print(result)