l = list()

for _ in range(5):
    l.append(int(input()))

print(int(sum(l)/5))
l.sort()
print(l[2])