#include <iostream>
#include <vector>
#include <map>

using namespace std;

// Since there can be up to 10 ** 5 employees, there can be up to ~10 ** 10
// unique disputes. To represent the worst case where all of them are resolved
// by the CEO, we need to use 64 bits instead.
typedef long long ll;

ll find_branch_size_dfs(int id, vector<vector<int>> &subordinates, vector<ll> &branch_sizes);
ll disputes_resolved_by(int id, vector<vector<int>> &subordinates, vector<ll> &branch_sizes);

ll solve(int N, vector<int> M) {
    vector<vector<int>> subordinates(N);
    for (size_t i = 1; i < M.size(); i++) {
        subordinates[M[i]].push_back(i);
    }
    
    vector<ll> branch_sizes(N, 0);
    find_branch_size_dfs(0, subordinates, branch_sizes);
    
    ll most_disputes = 0;
    for (int i = 0; i < N; i++) {
        most_disputes = max(most_disputes, disputes_resolved_by(i, subordinates, branch_sizes));
    }
    return most_disputes;
}

ll find_branch_size_dfs(int id, vector<vector<int>> &subordinates, vector<ll> &branch_sizes) {
    branch_sizes[id] = 1;
    for (int sub : subordinates[id]) {
        branch_sizes[id] += find_branch_size_dfs(sub, subordinates, branch_sizes);
    }
    return branch_sizes[id];
}

ll disputes_resolved_by(int id, vector<vector<int>> &subordinates, vector<ll> &branch_sizes) {
    ll self_disputes = branch_sizes[id] - 1;
    
    ll sum_branch_sizes = 0;
    for (int sub : subordinates[id]) {
        sum_branch_sizes += branch_sizes[sub];
    }
    ll cross_branch_disputes = 0;
    for (int sub : subordinates[id]) {
        sum_branch_sizes -= branch_sizes[sub];
        cross_branch_disputes += branch_sizes[sub] * sum_branch_sizes;
    }
    
    return self_disputes + cross_branch_disputes;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;

        vector<int> M(N);
        for (int &manager: M) {
            cin >> manager;
        }

        cout << solve(N, M) << '\n';
    }

    return 0;
}
