#include <iostream>

using namespace std;

int solve(int N) {
    int day = 0, bars = N;
    while (bars - day - 1 >= 0) {
        day++;
        bars -= day;
    }
    return day;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        cout << solve(N) << '\n';
    }
}
