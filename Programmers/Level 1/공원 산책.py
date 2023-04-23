def solution(park, routes):
    pos = []
    width = len(park[0]) - 1
    height = len(park) - 1

    for h, pk in enumerate(park):
        if "S" in pk:
            pos = [h, pk.index("S")]
            break

    for r in routes:
        way, n = r.split(" ")
        n = int(n)

        if way == "E":
            if pos[1] + n <= width:
                for i in range(1, n + 1):
                    if park[pos[0]][pos[1] + i] == "X":
                        break
                else:
                    pos[1] += n
        elif way == "W":
            if pos[1] - n >= 0:
                for i in range(1, n + 1):
                    if park[pos[0]][pos[1] - i] == "X":
                        break
                else:
                    pos[1] -= n
        elif way == "S":
            if pos[0] + n <= height:
                for i in range(1, n + 1):
                    if park[pos[0] + i][pos[1]] == "X":
                        break
                else:
                    pos[0] += n
        else:
            if pos[0] - n >= 0:
                for i in range(1, n + 1):
                    if park[pos[0] - i][pos[1]] == "X":
                        break
                else:
                    pos[0] -= n

    return pos
