from typing import List

COUNTS_AND_PATTERNS = {}

def solve(N: int, S: List[int], W: List[str]) -> None:
    word_bank = [[] for _ in range(10)]
    for i in range(N):
        word_bank[S[i]].append(W[i])
    
    found = False
    for counts, pattern in COUNTS_AND_PATTERNS.items():
        if all(len(word_bank[s]) >= counts[s] for s in range(1, 10)):
            found = True
            break
    
    if found:
        print(' '.join(word_bank[s].pop() for s in pattern[0]))
        print(' '.join(word_bank[s].pop() for s in pattern[1]))
        print(' '.join(word_bank[s].pop() for s in pattern[2]))
    else:
        print('IMPOSSIBLE\nIMPOSSIBLE\nIMPOSSIBLE')

def main():
    make_patterns()
    
    T = int(input())
    for _ in range(T):
        N = int(input())
        S, W = [], []
        for _ in range(N):
            s, w = input().split(' ')
            S.append(int(s))
            W.append(w)
        solve(N, S, W)

def make_patterns():
    global COUNTS_AND_PATTERNS
    
    fives = partitions(5)
    sevens = partitions(7)
    for line1 in fives:
        for line2 in sevens:
            for line3 in fives:
                pattern = (line1, line2, line3)
                counts = get_syllable_counts(pattern)
                if counts not in COUNTS_AND_PATTERNS:
                    COUNTS_AND_PATTERNS[counts] = pattern

def partitions(n):
    # Finds all ways to break n into pieces of at most k
    def make_partitions(n, k):
        if n == 0:
            return [[]]
        if k == 0 or n < 0:
            return []
        
        all_partitions = make_partitions(n - k, k)
        for w in all_partitions:
            w.append(k)
        all_partitions.extend(make_partitions(n, k - 1))
        
        return all_partitions
    return make_partitions(n, n)

def get_syllable_counts(pattern):
    counts = [0 for _ in range(10)]
    for line in pattern:
        for syllable in line:
            counts[syllable] += 1
    return tuple(counts)

if __name__ == '__main__':
    main()
