
n = int(input())

line = 1
count = 1

while n > count:
    count += line*6
    line += 1

print(line)