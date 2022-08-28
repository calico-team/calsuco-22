#include <iostream>
#include <vector>

using namespace std;

// Note that we need to use long long values when performing modular arithmetic
// to prevent multiplication overflow.
typedef long long ll;

// Forward declare for reading clarity
char move_that_beats(char move);
char get_lcg_move();
void crack_lcg();
ll construct_x(int index);
ll modular_inverse(ll x, ll m);

// Variables to track moves
int round_num = 0;
char my_history[100000], bot_history[100000];

// Variables to track and crack LCG
bool lcg_already_cracked = false;
int rand_index = 0;
char bot_rand_history[19 * 3];
bool next_bot_move_is_random = false;
ll x, a, c;
ll m = 1000000007;
vector<int> q;

char play_move() {
    char move;
    if (round_num >= 2 && my_history[round_num - 1] == my_history[round_num - 2]) {
        move = move_that_beats(move_that_beats(my_history[round_num - 1]));
    } else if (round_num >= 2 && bot_history[round_num - 1] == bot_history[round_num - 2]) {
        move = bot_history[round_num - 1];
    } else {
        if (round_num == 0) {
            move = 'R';
        } else if (lcg_already_cracked) {
            move = move_that_beats(get_lcg_move());
        } else {
            move = my_history[round_num - 1];
        }
        
        next_bot_move_is_random = true;
    }
    
    my_history[round_num] = move;
    return move;
}

void read_bot_move(char bot_move) {
    bot_history[round_num] = bot_move;
    
    if (next_bot_move_is_random && !lcg_already_cracked) {
        bot_rand_history[rand_index] = bot_move;
        rand_index++;
        
        if (rand_index == 19 * 3) {
            crack_lcg();
            lcg_already_cracked = true;
        }
        
        next_bot_move_is_random = false;
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {        
        char my_move;
        my_move = play_move();
        cout << my_move << endl;
        
        char bot_move;
        cin >> bot_move;
        read_bot_move(bot_move);
        
        round_num++;
    }
}

char move_that_beats(char move) {
    switch (move) {
        case 'R':
            return 'P';
        case 'P':
            return 'S';
        default:
            return 'R';
    }
}

char get_lcg_move() {
    if (q.empty()) {
        x = (a * x + c) % m;
        int temp = x;
        for (int i = 0; i < 19; i++) {
            q.push_back(temp % 3);
            temp /= 3;
        }
    }
    int move = q.back();
    q.pop_back();
    switch (move) {
        case 0:
            return 'R';
        case 1:
            return 'P';
        default:
            return 'S';
    }
}

void crack_lcg() {
    ll x0 = construct_x(0), x1 = construct_x(1), x2 = construct_x(2);
    ll x2_minus_x1 = (x2 - x1 + m) % m;
    ll x1_minus_x0 = (x1 - x0 + m) % m;
    
    a = x2_minus_x1 * modular_inverse(x1_minus_x0, m) % m;
    c = ((x1 - x0 * a) % m + m) % m;
    x = x2;
}

ll construct_x(int index) {
    ll x = 0;
    for (int i = 19 * index; i < 19 * (index + 1); i++) {
        x *= 3;
        switch (bot_rand_history[i]) {
            case 'R':
                x += 0;
                break;
            case 'P':
                x += 1;
                break;
            default:
                x += 2;
        }
    }
    return x;
}

// Adapted from the iterative Extended Euclidean GCD algorithm found at
// https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
ll modular_inverse(ll a, ll m) {
    ll m0 = m;
    ll y = 0, x = 1;
    
    if (m == 1)
        return 0;
    
    while (a > 1) {
        ll q = a / m;
        ll t = m;
        m = a % m;
        a = t;
        t = y;
        y = x - q * y;
        x = t;
    }
    
    return (x + m0) % m0;
}
