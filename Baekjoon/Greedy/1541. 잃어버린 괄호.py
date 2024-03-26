import sys
input = sys.stdin.readline

sics = list(input().strip().split("-"))
numbers = []
for sic in sics:
    if "+" in sic:
        numbers.append(sum(map(int, sic.split("+"))))
        continue
    numbers.append(int(sic))

result = numbers[0]
for number in numbers[1:]:
    result -= number
print(result)