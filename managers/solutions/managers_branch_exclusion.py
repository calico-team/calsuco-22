from typing import List

def solve(N: int, M: List[int]) -> int:
    subordinates = [[] for _ in range(N)]
    for i in range(1, N):
        subordinates[M[i]].append(i)
    
    branch_sizes = [None for _ in range(N)]
    def find_branch_size_dfs(id):
        branch_sizes[id] = 1
        for sub in subordinates[id]:
            branch_sizes[id] += find_branch_size_dfs(sub)
        return branch_sizes[id]
    find_branch_size_dfs(0)
    
    def disputes_resolved_by(id):
        self_disputes = branch_sizes[id] - 1
        
        sum_branch_sizes = 0
        for sub in subordinates[id]:
            sum_branch_sizes += branch_sizes[sub]
        cross_branch_disputes = 0
        for sub in subordinates[id]:
            cross_branch_disputes += branch_sizes[sub] * (sum_branch_sizes - branch_sizes[sub])
        cross_branch_disputes //= 2
        
        return self_disputes + cross_branch_disputes
    
    best = 0
    for i in range(N):
        best = max(best, disputes_resolved_by(i))
    return best

def main():
    T = int(input())
    for _ in range(T):
        N = int(input().strip())
        M = [int(x) for x in input().strip().split(' ')]
        print(solve(N, M))

if __name__ == '__main__':
    main()
