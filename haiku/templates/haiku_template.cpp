#include <iostream>
#include <vector>

using namespace std;

/**
 * Construct and output a haiku
 * 
 * N: the number of words
 * S: the list of syllables for each word
 * W: the words themselves
 */
void solve(int N, vector<int> &S, vector<string> &W) {
    // YOUR CODE HERE
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
