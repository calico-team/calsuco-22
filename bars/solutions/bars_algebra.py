import math

def solve(N: int) -> int:
    return int(0.5 * (math.sqrt(8 * N + 1) - 1))

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))

if __name__ == '__main__':
    main()
