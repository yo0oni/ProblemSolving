def solution(name, yearning, photos):
    answer = [0] * len(photos)
    score = dict()
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    print(score)
    for idx, photo in enumerate(photos):
        for people in photo:
            if people in score:
                answer[idx] += score[people]
            else:
                continue
    return answer