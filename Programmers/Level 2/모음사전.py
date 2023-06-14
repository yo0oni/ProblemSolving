from itertools import product

def solution(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    perm = []
    for i in range(1, len(alphabet)+1):
        for j in product(alphabet, repeat=i):
            perm.append(''.join(j))
            
    perm.sort()
    
    return perm.index(word) + 1