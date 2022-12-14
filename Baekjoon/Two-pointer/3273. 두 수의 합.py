import sys

n = int(sys.stdin.readline())
seq = sorted(list(map(int, sys.stdin.readline().split())))
sum_ = int(sys.stdin.readline())
result = 0
start = 0
end = len(seq)-1

while start < end:
    if seq[start] + seq[end] == sum_:
        result +=1
        start += 1
        end -= 1
    
    elif seq[start] + seq[end] < sum_:
        start += 1

    else:
        end -= 1

print(result)