def solution(nums):
    answer = 0
    length = len(nums)//2
    while len(set(nums)) > length:
        nums.pop()
    answer = len(set(nums))
    return answer