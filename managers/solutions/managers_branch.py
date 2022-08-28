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
        if len(subordinates[id]) == 0:
            return 0
        elif len(subordinates[id]) == 1:
            self_disputes = branch_sizes[id] - 1
            return self_disputes
        else:
            self_disputes = branch_sizes[id] - 1
            
            left_branch_size = branch_sizes[subordinates[id][0]]
            right_branch_size = branch_sizes[subordinates[id][1]]
            cross_branch_disputes = left_branch_size * right_branch_size
            
            return self_disputes + cross_branch_disputes
    
    return max(disputes_resolved_by(i) for i in range(N))

def main():
    T = int(input())
    for _ in range(T):
        N = int(input().strip())
        M = [int(x) for x in input().strip().split(' ')]
        print(solve(N, M))

if __name__ == '__main__':
    main()
