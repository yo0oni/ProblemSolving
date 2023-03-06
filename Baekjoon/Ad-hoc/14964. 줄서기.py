import sys
input = sys.stdin.readline

N, M = map(int, input().split())
student = [0] * N

for i in range(N):
    student[i] = i+1
    
for i in range(M):
    s1, s2 = map(int, input().split())
    student[s1-1] = student[s1-1] + 1
    student[s2-1] = student[s2-1] - 1

if len(set(student)) == N:
    print(*student)
else:
    print("-1")
