from typing import List

import itertools

def solve(N: int, S: List[int], W: List[str]) -> None:
    found = False
    for assignment in itertools.product(range(4), repeat=N):
        if sum(S[i] for i in range(N) if assignment[i] == 1) == 5 and \
            sum(S[i] for i in range(N) if assignment[i] == 2) == 7 and \
            sum(S[i] for i in range(N) if assignment[i] == 3) == 5:
            found = True
            break
    
    if found:
        print(' '.join(W[i] for i in range(N) if assignment[i] == 1))
        print(' '.join(W[i] for i in range(N) if assignment[i] == 2))
        print(' '.join(W[i] for i in range(N) if assignment[i] == 3))
    else:
        print('IMPOSSIBLE\nIMPOSSIBLE\nIMPOSSIBLE')

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
