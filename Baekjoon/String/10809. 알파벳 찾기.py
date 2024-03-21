import sys
input = sys.stdin.readline

s = list(input().strip())
alphabet = []
for _ in range(26):
    alphabet.append(-1)

number = 0
for i in s:
    if alphabet[ord(i) - 97] == -1:
        alphabet[ord(i) - 97] = number
    number += 1

print(*alphabet)