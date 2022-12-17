n, k = map(int, input().split())
student = [[0]*2 for _ in range(6)] #성별2개 6학년
room = 0

for _ in range(n):
    s,y= map(int, input().split())
    student[y-1][s-1] += 1

for i in range(6):
    for j in range(2):
        if student[i][j]%k == 0:
            room += student[i][j]/k
        else:
            room += student[i][j]//k + 1

print(int(room))