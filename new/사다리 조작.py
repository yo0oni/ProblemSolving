import sys
input = sys.stdin.readline

# 사다리를 안 두어도 정답이 될 수 있음
def check():
    for sj in range(1, N+1):
        j = sj
        for i in range(1, H+1):
            if arr[i][j]==1:
                j+=1
            elif arr[i][j-1]==1:
                j-=1
        if j!=sj:
            return 0
    return 1

def dfs(n, s):
    global ans
    if ans==1:
        return

    if n==cnt: 
        if check()==1:
            ans=1
        return

    for j in range(s, CNT):
        ti,tj = pos[j]

        if arr[ti][tj-1]==0 and arr[ti][tj+1]==0:
            arr[ti][tj]=1
            dfs(n+1, j+1)
            arr[ti][tj]=0

N, M, H = map(int, input().split())

arr = [[0]*(N+2) for _ in range(H+1)]
for _ in range(M):
    ti,tj = map(int, input().split())
    arr[ti][tj]=1

pos = []
for i in range(1, H+1):
    for j in range(1, N+1):
        if arr[i][j]==0 and arr[i][j-1]==0 and arr[i][j+1]==0:
            pos.append((i,j))
CNT = len(pos)

for cnt in range(4):
    ans = 0
    dfs(0,0)
    if ans==1:
        ans = cnt
        break
else:
    ans = -1
print(ans)