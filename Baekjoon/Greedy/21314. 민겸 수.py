import sys
input = sys.stdin.readline

strings = list(input().strip())

temp = ""
before = 0
big_values = []
for index, string in enumerate(strings):
    temp += string

    if string == "K":
        big_values.append(temp)
        temp = ""
    
    if index == len(strings) - 1 and temp != "":
        for _ in range(len(temp)):
            big_values.append("M")

answer = ""
for value in big_values:
    if "K" in value:
        answer += str(5 * (10 ** value.count("M")))
    else:
        answer += str(10 ** (value.count("M")-1))
print(answer)


temp = ""
before = 0
small_values = []
for index, string in enumerate(strings):
    if string == "M":
        temp += string

    if string == "K":
        small_values.append(temp)
        small_values.append("K")
        temp = ""

    if index == len(strings) - 1 and temp != "":
        small_values.append(temp)

small_values = [value for value in small_values if value != ""]
answer = ""

for value in small_values:
    if "K" in value:
        answer += str(5 * (10 ** value.count("M")))
    else:
        answer += str(10 ** (value.count("M")-1))
print(answer)
