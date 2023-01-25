n = input()

# 각 문자열마다 ppap를 넣어본다?
# ppap가 보이면 p로 바꾸기?
# 본인 기준으로 +3 위치까지 ppap인가?
# ppap임 -> p로 바꿔줌
# 그렇게 다 바꿧는데 마지막에 ppap 가 남으면 ok
# 아니면 np

result = []
ppap = ["P", "P", "A", "P"]

for i in range(len(n)):
    result.append(n[i])
    if result[-4:] == ppap:
        for _ in range(3):
            result.pop() # 이러면 P만 남고 다 지워짐!
    # if i+4 <= len(ppap):
        # if ppap[i:i+4] == "PPAP":
            # result = ppap.replace("PPAP","P")
            # ppap = list(ppap)
            # ppap[i] = "P"
            # ppap[i+1:i+4] = ""
            # result = ''.join(ppap)

if result == ppap or result == ["P"]:
    print("PPAP")
else:
    print("NP")