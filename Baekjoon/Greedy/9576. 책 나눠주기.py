t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    checked = [0] * (n+1)
    book = []
    for _ in range(m):
        start, end = map(int, input().split())
        book.append((start, end))

    book.sort(key=lambda x: x[1])

    count = 0

    for a, b in book:
        for i in range(a, b+1):
            if not checked[i]:
                checked[i] = 1
                count += 1
                break # 반복문 하나만 종료

    print(count)