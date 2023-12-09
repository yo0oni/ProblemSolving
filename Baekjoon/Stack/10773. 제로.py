import sys
input = sys.stdin.readline

# 재민 = 장부 관리
# 재현 = 돈 관리 -> 잘못된 수를 부를 때마다 0을 외침 -> 재민이가 가장 최근에 쓴거 삭제

N = int(input())
stack = []
for _ in range(N):
    number = int(input())
    if number != 0:
        stack.append(number)
    
    else:
        stack.pop()

print(sum(stack))