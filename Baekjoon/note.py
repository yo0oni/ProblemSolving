def dfs(index, arr):
    if index == len(kriii):
        print(*arr)
        exit()

    # 1자리수 check
    num1 = int(kriii[index])
    if not visited[num1]:
        print(arr)
        visited[num1] = True
        arr.append(num1)
        dfs(index + 1, arr)
        visited[num1] = False
        arr.pop()

    # 2자리수 check
    if index+1 < len(kriii):
        num2 = int(kriii[index:index+2])
        if num2 <= N and not visited[num2]:
            visited[num2] = True
            arr.append(num2)
            dfs(index+2, arr)
            visited[num2] = False
            arr.pop()


kriii = input()
N = len(kriii) if len(kriii) < 10 else 9 + (len(kriii) - 9) // 2
visited = [0 for _ in range(N + 1)]

dfs(0, [])