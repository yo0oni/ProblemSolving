from sys import stdin
input = stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

while len(S) != len(T):
    if T[-1] == "A":
        T.pop()
    else:
        T.pop()
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)