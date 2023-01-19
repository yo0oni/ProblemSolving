from itertools import combinations

n = int(input())

def decrease(n):
    for i in range(10):
        numbers.append(i)
    for i in range(2,11):
        for j in combinations(range(10),i):
            numbers.append(int(''.join(map(str, ((j)[::-1])))))
    numbers.sort()
    # print(len(numbers))
    if n>=1023:
        print("-1")
    else:
        print(numbers[n])


numbers = []
decrease(n)