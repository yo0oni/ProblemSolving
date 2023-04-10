def solution(lottos, win_nums):
    lotto = {6:1, 5:2, 4:3, 3:4, 2:5, 1: 6, 0: 6} # 6개일 때 1등
    top = lotto[len(set(lottos)&set(win_nums))+lottos.count(0)]
    low = lotto[len(set(lottos)&set(win_nums))]
    return top, low