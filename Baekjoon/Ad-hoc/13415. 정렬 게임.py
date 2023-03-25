import sys, heapq
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
K = int(input())
sort_section = list(map(int, input().split()))
heapq.heapify(numbers)
print(numbers)
flag = True

for i in sort_section:
    # i == 3, 2
    temp = numbers[:i]
    back = numbers[i:]
    if flag:
        temp.sort()
        flag = False
    else:
        temp.sort(reverse=True)
        flag = True
    numbers = temp + back
print(numbers)