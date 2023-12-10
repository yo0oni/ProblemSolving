while True:
    string = input()
    stack = []

    if string == ".":
        break
    
    for word in string:
        if word == "(" or word == "[":
            stack.append(word)
            
        elif word == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(word)
                break

        elif word == ")":
            if stack and stack[-1] =="(":
                stack.pop()
            else:
                stack.append(word)
                break

    if len(stack) == 0:
        print("yes")

    else:
        print("no")
