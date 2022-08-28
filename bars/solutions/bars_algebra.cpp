#include <iostream>
#include <math.h>

using namespace std;

// Note that we change the type of N here to double
int solve(double N) {
    return (int) (0.5 * (sqrt(8 * N + 1) - 1));
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        double N;
        cin >> N;
        cout << solve(N) << '\n';
    }
}
