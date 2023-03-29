import sys

input = sys.stdin.readline

n = int(input())
i = 1
number = 666

while i != n:
    number += 1
    if '666' in str(number):
        i += 1
print(number)