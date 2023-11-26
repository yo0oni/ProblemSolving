import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [0]
segment_tree = [0]*(N*4)

for _ in range(N):
    numbers.append(int(input()))

def init(start, end, index):
    if start == end:
        segment_tree[index] = numbers[start]
        return segment_tree[index]
	
    mid = (start+end) // 2
    segment_tree[index] = min(init(start, mid, index*2), init(mid+1, end, index*2+1))
    return segment_tree[index]


def find(start, end, index, left, right):
    if start > right or end < left:
        return sys.maxsize
        
    if start >= left and end <= right:
        return segment_tree[index]

    mid = (start + end) // 2
    return min(find(start, mid, index*2, left, right), find(mid+1, end, index*2+1, left, right))

init(1, N, 1)

for _ in range(M):
    a, b = map(int, input().split())
    print(find(1, N, 1, a, b))