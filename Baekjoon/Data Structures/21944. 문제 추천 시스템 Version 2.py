# import heapq
# import sys
# input = sys.stdin.readline

# N = int(input())
# easy, hard, g_easy, g_hard = [], [], [], []
# check = dict()
# for _ in range(N):
#     P, L, G = map(int, input().split())
#     heapq.heappush(easy, (L,P,G))
#     heapq.heappush(hard, (-L, -P, G))
#     check[P] = True

# M = int(input())
# for i in range(M):
#     command = list(map(str,input().split()))
#     if command[0] == "add":
#      # L P G
#         heapq.heappush(easy, (int(command[2]), int(command[1]), int(command[3])))
#         heapq.heappush(hard, (-int(command[2]), -int(command[1]), int(command[3])))
#         # print(easy, hard, sep="\n")
#         check[int(command[1])] = True
        
#     elif command[0] == "recommend":
#         temp = []
#         if command[2] == "1":
#             for i in range(len(hard)):
#                 some = heapq.heappop(hard)
#                 temp.append(some)
#                 if some[2] == int(command[1]):
#                     if check[some[1] * -1]: 
#                         print(some[1] * -1)
#                         break
#             for i in range(len(temp)):
#                 heapq.heappush(hard, temp[i])
            
#         else:
#             for i in range(len(easy)):
#                 some = heapq.heappop(easy)
#                 temp.append(some)
#                 if some[2] == int(command[1]):
#                     if check[some[1]]: 
#                         print(some[1])
#                         break
#             for i in range(len(temp)):
#                 heapq.heappush(easy, temp[i])

#     elif command[0] == "recommend2":
#         temp = []
#         # 가장 어려운 문제
#         if command[1] == "1":
#             for i in range(len(hard)):
#                 some = heapq.heappop(hard)
#                 temp.append(some)
#                 if check[some[1] * -1]:
#                     print(some[1] * -1)
#                     break
#             for i in range(len(temp)):
#                 heapq.heappush(hard, temp[i])
#         else:
#             for i in range(len(easy)):
#                 some = heapq.heappop(easy)
#                 temp.append(some)
#                 if check[some[1]]:
#                     print(some[1])
#                     break
#             for i in range(len(temp)):
#                 heapq.heappush(easy, temp[i])

#     elif command[0] == "recommend3":
#         temp = []       
#         if command[1] == "1": # 쉬운 문제
#             for i in range(len(easy)):
#                 some = heapq.heappop(easy)
#                 temp.append(some)
#                 if some[0] >= int(command[2]):
#                     if check[some[1]]:
#                         print(some[1])
#                         break
#                     else:
#                         print("-1")
#                         break

#             for i in range(len(temp)):
#                 heapq.heappush(easy, temp[i])

#         else:
#             for i in range(len(hard)):
#                 some = heapq.heappop(hard)
#                 temp.append(some)
#                 if some[0]*-1 <= int(command[2]):
#                     if check[some[1]*-1]:
#                         print(some[1]*-1)
#                         break
#                     else:
#                         print("-1")
#                         break

#             for i in range(len(temp)):
#                 heapq.heappush(hard, temp[i])


#     elif command[0] == "solved":
#         check[int(command[1])] = False
