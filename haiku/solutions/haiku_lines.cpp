#include <iostream>
#include <vector>

using namespace std;

void solve(int N, vector<int> &S, vector<string> &W) {
    bool found = false;
    int assignment = 0;
    for (; assignment < 1 << (N * 2); assignment++) {
        int line_syllables[4] = {0, 0, 0, 0};
        for (int i = 0; i < N; i++) {
            line_syllables[(assignment >> (i * 2)) & 3] += S[i];
        }
        if (line_syllables[1] == 5 && line_syllables[2] == 7 && line_syllables[3] == 5) {
            found = true;
            break;
        }
    }
    
    if (found) {
        for (int line = 1; line <= 3; line++) {
            for (int i = 0; i < N; i++) {
                if (((assignment >> (i * 2)) & 3) == line) {
                    cout << W[i] << ' ';
                }
            }
            cout << '\n';
        }
    } else {
        cout << "IMPOSSIBLE\nIMPOSSIBLE\nIMPOSSIBLE\n";
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        
        vector<int> S;
        vector<string> W;
        for (int j = 0; j < N; j++) {
            int s;
            cin >> s;
            S.push_back(s);
            string w;
            cin >> w;
            W.push_back(w);
        }
        
        solve(N, S, W);
    }
}
