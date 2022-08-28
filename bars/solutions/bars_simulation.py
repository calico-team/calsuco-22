def solve(N: int) -> int:
    day, bars = 0, N
    while bars - day - 1 >= 0:
        day += 1
        bars -= day
    return day

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))

if __name__ == '__main__':
    main()
