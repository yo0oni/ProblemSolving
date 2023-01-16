# 4
# 1 2 3 4
def backtracking(sum):
    global answer
    if len(l) == 2: # 첫번째, 마지막 두개만 남음
        answer = max(answer, sum)
        # print(energy)
        return answer
    
    # 에너지가 가장 큰 합을 찾아야 함.. -> 하나하나씩 전부 ?

    for i in range(1, len(l)-1):
        sum_energy = int(l[i-1]) * int(l[i+1])
        energy = l[i]
        del l[i]
        backtracking(sum_energy + sum)
        l.insert(i, energy)
            

n = int(input())
l = list(input().split())
answer = 0
backtracking(0)
print(answer)