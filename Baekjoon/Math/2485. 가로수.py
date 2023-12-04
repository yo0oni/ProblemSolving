import sys, math
input = sys.stdin.readline

N = int(input())

street_trees = []

start = int(input())
for _ in range(N-1):
    tree = int(input())
    street_trees.append(tree - start)
    start = tree

differences_gcd = street_trees[0]
for difference in street_trees:
    differences_gcd = math.gcd(differences_gcd, difference)

count = 0
for tree in street_trees:
    count += tree // differences_gcd - 1

print(count)