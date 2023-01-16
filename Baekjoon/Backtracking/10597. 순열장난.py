# n = 4 1 11109876532

# 백트래킹에서 필요한 것들
# 입력값 n, 수열에 저장
def backtracking(index, answer):

    # 인덱스 == 순열 길이면 종료
    if index == len(sujin):
        print(*answer)
        exit()
    # 50이하이기 때문에 무조건 두자릿수 보장
    # 한자리씩
    number1 = int(sujin[index]) # 4, 1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2
    if not visited[number1]:
        visited[number1] = True
        answer.append(number1)
        backtracking(index+1, answer)
        visited[number1] = False
        answer.pop()

    # 두자리씩
    if index+1 < len(sujin):
        number2 = int(sujin[index:index+2])
        if number2<=max_num and not visited[number2]:
            visited[number2] = True
            answer.append(number2)
            backtracking(index+2, answer)
            visited[number2] = False
            answer.pop()

sujin = input()
max_num = len(sujin) if len(sujin) < 10 else 9 + (len(sujin) - 9) // 2
visited = [0] * 51
backtracking(0, [])