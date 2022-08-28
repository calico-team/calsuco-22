#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

/**
 * Find the most possible disputes a single employee is responsible for 
 * resolving at the company.
 * 
 * N: the number of employees in the company
 * M: the list of integers denoting the employee number of each individual's manager
 */
ll solve(int N, vector<int> M) {
    // YOUR CODE HERE
    return 0;
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
