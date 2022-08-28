from typing import List

def solve(N: int, M: List[int]) -> int:
    '''
    Find the most possible disputes a single employee is responsible for 
    resolving at the company.
    
    N: the number of employees in the company
    M: the list of integers denoting the employee number of each individual's manager
    '''
    return 0

def main():
    T = int(input())
    for _ in range(T):
        N = int(input().strip())
        M = [int(x) for x in input().strip().split(' ')]
        print(solve(N, M))

if __name__ == '__main__':
    main()
