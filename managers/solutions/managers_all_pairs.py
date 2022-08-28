from typing import List

def solve(N: int, M: List[int]) -> int:
    def who_resolves(a, b):
        management_chain = set([0])
        while a != 0:
            management_chain.add(a)
            a = M[a]
        while b not in management_chain:
            b = M[b]
        return b
    disputes = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            disputes[who_resolves(i, j)] += 1
    return max(disputes)

def main():
    T = int(input())
    for _ in range(T):
        N = int(input().strip())
        M = [int(x) for x in input().strip().split(' ')]
        print(solve(N, M))

if __name__ == '__main__':
    main()
