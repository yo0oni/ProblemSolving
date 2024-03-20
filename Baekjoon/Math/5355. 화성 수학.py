import sys, math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    inputs = list(input().split())
    number = float(inputs.pop(0))
    
    for oper in inputs:
        if oper == "@":
            number *= 3
        elif oper == "%":
            number += 5
        elif oper == "#":
            number -= 7
    
    print(format(number, ".2f"))