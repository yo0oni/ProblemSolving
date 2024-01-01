import sys
input = sys.stdin.readline

text = (input().strip()).upper()
word_set = set(list(text))
word_count = dict()

for word in word_set:
    word_count[word] = text.count(word)

sort_count = sorted(word_count.items(), key=lambda x: x[1])

if len(sort_count) > 1:
    first = sort_count.pop()
    second = sort_count.pop()

    if first[1] == second[1]:
        print("?")
    else:
        print(first[0])

else:
    print(sort_count.pop()[0])