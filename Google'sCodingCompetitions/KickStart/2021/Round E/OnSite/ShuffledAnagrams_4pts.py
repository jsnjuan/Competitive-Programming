from itertools import permutations

T = int(input())

def shuffle_anagram(A, B):
    for a, b in zip(A, B):
        if a==b:
            return False
    return True

def gen_sol(S):
    for p in permutations(S):
        p_cad = ''.join(p)
        if shuffle_anagram(p_cad, S):
            return p_cad
    return 'IMPOSSIBLE'


for i in range(T):
    S = input()
    sol = gen_sol(S)
    print(f"Case #{i+1}: {sol}")
