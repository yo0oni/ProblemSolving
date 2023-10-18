def duplicateZeros(arr):
    answer_temp = []
    
    for num in arr:
        if num == 0:
            answer_temp.append(num)
        answer_temp.append(num)
            
    answer = answer_temp[:len(arr)]
    
    for i in range(len(arr)):
        arr[i] = answer[i]