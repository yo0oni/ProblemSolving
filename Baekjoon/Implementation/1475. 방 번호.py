n = input()
card = [0]*10

for i in n:
    if i in ['6','9']:
        if card[6] <= card[9]:
            card[6] += 1
        else:
            card[9] += 1
    else:
        card[int(i)] += 1

print(max(card))