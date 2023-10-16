import sys
from collections import deque
input = sys.stdin.readline

s, p = map(int, input().split())
string = list(input().strip())
A, C, G, T = map(int, input().split())

dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
count = start = 0
end = p -1
password = list(string[start:end])

for str in password:
    dict[str] += 1
print(password, dict)

while end < s:
    dict[string[end]] += 1


    if dict['A'] >= A and dict['C'] >= C and dict['G'] >= G and dict['T'] >= T:
        count += 1

    dict[string[start]] -= 1
    start += 1
    end += 1

print(count)