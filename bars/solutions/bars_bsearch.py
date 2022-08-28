def solve(N: int) -> int:
    lo, hi, best = 0, N, 0
    while lo <= hi:
        guess = (hi + lo) // 2
        if guess * (guess + 1) // 2 <= N:
            best = guess
            lo = guess + 1
        else:
            hi = guess - 1
    return best

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))

if __name__ == '__main__':
    main()
