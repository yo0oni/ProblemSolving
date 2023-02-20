import sys
input = sys.stdin.readline

N = int(input())
u = [int(sys.stdin.readline()) for _ in range(N)]
u.sort()

u_sum = set()
for x in u:
    for y in u:
        u_sum.add(x+y)
# print(u_sum)

def sum_number():
    for i in range(N-1, -1, -1):
        for j in range(i+1):
            # print(i, j, u[i], u[j])
            if u[i]-u[j] in u_sum:
                return u[i]

print(sum_number())