import heapq
import sys
input = sys.stdin.readline

N = int(input())
# dict = dict()
easy, hard = [], []
check = {}
for _ in range(N):
    # 문제 번호, 난이도
    P, L = map(int, input().split())
    heapq.heappush(easy, (L,P))
    heapq.heappush(hard, (-L, -P))
    check[P] = True
# print(dict)
M = int(input())
for i in range(M):
    command = list(map(str,input().split()))
    if command[0] == "add":
        heapq.heappush(easy, (int(command[2]), int(command[1])))
        heapq.heappush(hard, (-int(command[2]), -int(command[1])))
        check[int(command[1])] = True
    elif command[0] == "recommend":
        temp = []
        if command[1] == "1":
            for i in range(len(hard)):
                some = heapq.heappop(hard)
                temp.append(some)
                if check[some[1] * -1]:
                    print(some[1] * -1)
                    break
            for i in range(len(temp)):
                heapq.heappush(hard, temp[i])
        else:
            for i in range(len(easy)):
                print(easy)
                some = heapq.heappop(easy)
                temp.append(some)
                
                if check[some[1]]:
                    print(some[1])
                    break
            for i in range(len(temp)):
                heapq.heappush(easy, temp[i])           
    elif command[0] == "solved":
        if int(command[1]) == (hard[0][1]*-1):
            heapq.heappop(hard)
            # print(easy, hard, sep='\n')
        elif int(command[1]) == (easy[0][1]):
            heapq.heappop(easy)
            # print(easy, hard, sep='\n')
        