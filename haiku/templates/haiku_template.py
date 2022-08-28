from typing import List

def solve(N: int, S: List[int], W: List[str]) -> None:
    '''
    Construct and output a haiku
    
    N: the number of words
    S: the list of syllables for each word
    W: the words themselves
    '''
    # YOUR CODE HERE
    return

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
