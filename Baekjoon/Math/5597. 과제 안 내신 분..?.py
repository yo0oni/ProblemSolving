import sys
input = sys.stdin.readline

students = []
for i in range(1, 31):
    students.append(i)

for _ in range(28):
    student = int(input())
    students.remove(student)

print(*students)