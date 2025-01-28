import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    parent_x = find_parent(parent, x)
    parent_y = find_parent(parent, y)

    if parent_x < parent_y:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y


def solution(n, costs):
    parent = [i for i in range(n+1)]
    costs.sort(key=lambda x: x[0])

    sum = 0
    max = 0
    count = 0
    n_1 = n - 1

    for cost, a, b in costs:

        root_a = find_parent(parent, a)
        root_b = find_parent(parent, b)

        if root_a == root_b:
            continue

        union_parent(parent, root_a, root_b)
        sum += cost
        max = cost
        count += 1

        if count == n_1:
            break

    return sum - max


def main():
    n, m = map(int, input().split())

    costs = []
    for _ in range(m):
        a, b, cost = map(int, input().split())
        costs.append((cost, a, b))
    
    print(solution(n, costs))


if __name__ == "__main__":
    main()