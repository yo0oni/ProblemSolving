def solution(n, arr1, arr2):
    answer = []
    result = []
    
    for i in range(len(arr1)):
        binaryNum1 = int(bin(arr1[i])[2:])
        binaryNum2 = int(bin(arr2[i])[2:])
        answer.append((str(binaryNum1 + binaryNum2).zfill(n)))

    for i in answer:
        string = ''
        for j in range(len(i)):
            if i[j] != '0':
                string += "#"
            else:
                string += " "
        result.append(string)

    return result