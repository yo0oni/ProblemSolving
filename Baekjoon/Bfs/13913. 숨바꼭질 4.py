from collections import deque

def bfs():
    count = 0
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x==k:
            print(time[x])
            # 무조건 밑에서 올라가야 한다고 생각했다!!!!
            # 위에서 내려오기엔 경우의 수가 너무 많아서 메모리 초과가 날 것 같다
            ans = []
            while x != n:
                ans.append(x) # 17 추가
                x = route[x] # 17에 도달하기 이전 값 추가 == 16, 그 다음은 16 이전인 8
            ans.append(n) # 출발점일땐 조건문 해당하지 않아서 빠지므로 따로 추가
            ans.reverse()  # 역순으로 저장되어 있으므로 순서를 바꿔주기
            print(' '.join(map(str, ans)))
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i <= max_num and not time[i]:
                # 지나온 노드를 알기 위해 기록
                route[i] = x
                time[i] = time[x] + 1
                queue.append(i)

max_num = 100000
time = [0] * (max_num+1)
route = [0] * (max_num+1)
n, k = map(int, input().split())
bfs()