# import sys, heapq

# n, h_centi, t = map(int, sys.stdin.readline().split())
# h = []
# for _ in range(n):
#     h.append(-int(sys.stdin.readline()))
# heapq.heapify(h)

# count = 0
# for _ in range(t):
#     if -h[0] > h_centi:
#         # h[0] = h[0]//2
#         # h.sort(reverse=True)
#         heapq.heapreplace(h, -(-h[0] // 2))
#         count += 1
#     else:
#         break

# if -h[0] >= h_centi:
#     print('NO', -h[0], sep='\n')
# else:
#     print('YES', count, sep='\n')

import sys, heapq

n, h_centi, t = map(int, sys.stdin.readline().split())
h = []
for _ in range(n):
    h.append(-int(sys.stdin.readline()))
heapq.heapify(h)

count = 0
for _ in range(t):
    if -h[0] == 1 or -h[0] < h_centi:
        break
    else:
        # h[0] = h[0]//2
        # h.sort(reverse=True)
        heapq.heapreplace(h, -(-h[0] // 2))
        count += 1

if -h[0] >= h_centi:
    print('NO', -h[0], sep='\n')
else:
    print('YES', count, sep='\n')