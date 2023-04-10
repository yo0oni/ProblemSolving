def solution(s):
    answer = ''
    word ={"zero":"0", "one" : "1", "two" :"2", "three" : "3", "four" :"4", "five" :"5", "six" : "6", "seven" : "7","eight" : "8","nine" : "9"}
    s = list(s)
    string = ''
    for i in s:
        number = 0
        try:
            number = int(i)
            answer += str(number)
        except:
            string += i
        if string in word:
            answer += word[string]
            string = ''
        
    return int(answer)