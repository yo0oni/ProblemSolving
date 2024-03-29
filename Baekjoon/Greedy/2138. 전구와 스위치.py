import sys
input = sys.stdin.readline

n = int(input())
switchs = list(map(int, input().strip()))
want = list(map(int, input().strip()))

def change(switchs, index):
    if index == 0:
        switchs[index] = 1 - switchs[index]
        switchs[index+1] = 1 - switchs[index+1]
    
    elif index == len(switchs) - 1:
        switchs[index] = 1 - switchs[index]
        switchs[index-1] = 1 - switchs[index-1]
    
    else:
        switchs[index] = 1 - switchs[index]
        switchs[index-1] = 1 - switchs[index-1]
        switchs[index+1] = 1 - switchs[index+1]

# 0번 인덱스를 누르지 않는 경우
answer_1 = 0
answer_1_switch = switchs.copy()
for index in range(1, len(switchs)):
    if answer_1_switch[index-1] != want[index-1]:
        change(answer_1_switch, index)
        answer_1 += 1

if answer_1_switch != want:
    answer_1 = 1e9

# 0번 인덱스를 누르는 경우
answer_2 = 1 # 0번 인덱스를 누르고 시작하기 때문에 answer_2는 1로 선언한다.
change(switchs, 0) # 0번 인덱스 눌러주기
for index in range(1, len(switchs)):
    if switchs[index-1] != want[index-1]:
        change(switchs, index)
        answer_2 += 1

if switchs != want:
    answer_2 = 1e9

result = min(answer_1, answer_2)
print(result if result != 1e9 else -1)