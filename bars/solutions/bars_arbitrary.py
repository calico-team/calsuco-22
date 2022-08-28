import math

def solve(N: int) -> int:
    return (math.isqrt(8 * N + 1) - 1) // 2

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))

if __name__ == '__main__':
    main()
