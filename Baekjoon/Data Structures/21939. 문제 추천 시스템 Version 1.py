import heapq
import sys
input = sys.stdin.readline

# def system():


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
        # P = int(command[1])
        # L = int(command[2])
        # dict[P] = L
        # print(dict)
    elif command[0] == "recommend":
        # 가장 어려운 문제
        if command[1] == "1":
            print(hard[0][1] * -1)
        else:
            print(easy[0][1])
        #     value = dict.pop(max(dict.values()))
        #     print()
        # else:
        #     print(dict.pop(0))            
    elif command[0] == "solved":
        if int(command[1]) == (hard[0][1]*-1):
            heapq.heappop(hard)
            # print(easy, hard, sep='\n')
        elif int(command[1]) == (easy[0][1]):
            heapq.heappop(easy)
            # print(easy, hard, sep='\n')
        
        # del dict[command[1]]
