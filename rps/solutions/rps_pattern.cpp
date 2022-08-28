#include <iostream>

using namespace std;

int round_num = 0;

char play_move() {
    switch(round_num % 6) {
        case 0:
        case 1:
            return 'R';
        case 2:
        case 3:
            return 'S';
        default:
            return 'P';
    }
}

void read_bot_move(char bot_move) {
    // This strategy doesn't care about opponent moves, so we do nothing here
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
