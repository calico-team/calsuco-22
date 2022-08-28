import time

from typing import List

def solve(N: int, S: List[int], W: List[str]) -> None:
    N, S, W = filter_words(N, S, W)
    
    dp = [[[[] for _ in range(6)] for _ in range(8)] for _ in range(6)]
    dp[0][0][0] = [[], [], [], []]
    for i in range(N):
        dp2 = [[[[] for _ in range(6)] for _ in range(8)] for _ in range(6)]
        for line1 in range(6):
            for line2 in range(8):
                for line3 in range(6):
                    partial_haiku = dp[line1][line2][line3]
                    if partial_haiku:
                        dp2[line1][line2][line3] = partial_haiku
                        if line1 + S[i] <= 5:
                            dp2[line1 + S[i]][line2][line3] = copy_haiku(partial_haiku)
                            dp2[line1 + S[i]][line2][line3][1].append(i)
                        if line2 + S[i] <= 7:
                            dp2[line1][line2 + S[i]][line3] = copy_haiku(partial_haiku)
                            dp2[line1][line2 + S[i]][line3][2].append(i)
                        if line3 + S[i] <= 5:
                            dp2[line1][line2][line3 + S[i]] = copy_haiku(partial_haiku)
                            dp2[line1][line2][line3 + S[i]][3].append(i)
        dp = dp2
        
    if dp[5][7][5]:
        print(' '.join(W[i] for i in dp[5][7][5][1]))
        print(' '.join(W[i] for i in dp[5][7][5][2]))
        print(' '.join(W[i] for i in dp[5][7][5][3]))
    else:
        print('IMPOSSIBLE\nIMPOSSIBLE\nIMPOSSIBLE')

def filter_words(N, S, W):
    S_filtered, W_filtered = [], []
    allowed_syllable_counts = [0, 17, 7, 4, 3, 3, 1, 1, 0, 0];
    for i in range(N):
        if allowed_syllable_counts[S[i]] > 0:
            S_filtered.append(S[i])
            W_filtered.append(W[i])
            allowed_syllable_counts[S[i]] -= 1
    return len(S_filtered), S_filtered, W_filtered

def copy_haiku(haiku):
    return [list(line) for line in haiku]

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
