import sys
input = sys.stdin.readline

N = int(input())
words = []
check = []

for _ in range(N):
    word = input().strip()
    if word not in check:
        words.append((len(word), word))
        check.append(word)

words.sort(key=lambda x: (x[0], x[1]))

for index in range(len(words)):
    print(words[index][1])