import collections

t = int(input())
for _ in range(t):
    n = int(input())
    count = collections.defaultdict(int)
    numbers=list(map(int, input().split()))

    for number in numbers:
        count[number]+=1

    s_count = sorted(count.items(), key=lambda x:x[1], reverse=True)
    print(f"#{n} {s_count[0][0]}")
