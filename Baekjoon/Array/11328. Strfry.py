import sys, itertools
from itertools import permutations
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    string, want = map(str, input().split())
    want_list = list(want.strip())
    words = list(string.strip())

    flag = True
    for word in words:
        if word in want_list:
            want_list.remove(word)
        
    if want_list or len(string) > len(want):
        print("Impossible")
    else:
        print("Possible")