# 어차피 짝수개로 들어옴 (세트니까)
# 절반으로 갈라서 한쪽은 다 {
# 나머지 절반은 다 }
# 그리고 바뀐 애들 숫자 세기

# {{{{}}}} 이런애들 말고 {}{}{}{}{}{}{} 이런 애들도 고려해야됨......

number = 0
while True :
    count = 0
    open_stack = []
    str = input()
    if str.startswith('-'): # 포함 여부를 확인하여 멈춰주는 메소드
        break
    
    for s in str:
        if s == '{':
            open_stack.append(str)
        else: # 닫힌 괄호면
            if open_stack: # 비어있지 않으면
                open_stack.pop() # 열린 괄호가 들어있는 것이므로 둘이 합혀줌
            else: # 비어있으면
                open_stack.append("{")
                count += 1
    
    count += len(open_stack)//2 if len(open_stack) > 1 else len(open_stack)
    number += 1

    print(f"{number}. {count}")