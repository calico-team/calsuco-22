from typing import List

import itertools

def solve(N: int, S: List[int], W: List[str]) -> None:
    found = False
    for perm in itertools.permutations(range(N)):
        if is_perm_haiku(N, S, perm):
            found = True
            break
    
    if found:
        syllables, i = 0, 0
        for target in [5, 12, 17]:
            line = []
            while syllables < target:
                syllables += S[perm[i]]
                line.append(W[perm[i]])
                i += 1
            print(' '.join(line))
    else:
        print('IMPOSSIBLE\nIMPOSSIBLE\nIMPOSSIBLE')

def is_perm_haiku(N, S, perm):
    syllables, i = 0, 0
    for target in [5, 12, 17]:
        while syllables < target and i < N:
            syllables += S[perm[i]]
            i += 1
        if syllables != target:
            return False
    return True

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S, W = [], []
        for _ in range(N):
            s, w = input().split(' ')
            S.append(int(s))
            W.append(w)
        solve(N, S, W)

if __name__ == '__main__':
    main()
