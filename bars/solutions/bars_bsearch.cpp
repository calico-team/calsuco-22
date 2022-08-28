#include <iostream>

using namespace std;

// Note that we need to use long long values because N can exceed the maximum
// 32 bit integer.
typedef long long ll;

ll solve(ll N) {
    // We set hi to 32 bit INT_MAX instead of 64 bit LLONG_MAX to prevent
    // multiplication overflow. It can be proven that all answers for 2B are
    // smaller.
    ll lo = 0, hi = (1 << 31) - 1, best = 0;
    while (lo <= hi) {
        ll guess = (hi + lo) / 2;
        if (guess * (guess + 1) / 2 <= N) {
            best = guess;
            lo = guess + 1;
        } else {
            hi = guess - 1;
        }
    }
    return best;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        ll N;
        cin >> N;
        cout << solve(N) << '\n';
    }
}
