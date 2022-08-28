#include <iostream>

using namespace std;

int round_num = 0;
char my_history[100000], bot_history[100000];

char play_move() {
    char move;
    if (round_num >= 2 && my_history[round_num - 1] == my_history[round_num - 2]) {
        switch (my_history[round_num - 1]) {
            case 'R':
                move = 'S';
                break;
            case 'P':
                move = 'R';
                break;
            default:
                move = 'P';
        }
    } else if (round_num >= 2 && bot_history[round_num - 1] == bot_history[round_num - 2]) {
        move = bot_history[round_num - 1];
    } else {
        // The first move is random, so it doesn't matter what we play
        if (round_num == 0) {
            move = 'R';
        } else {
            move = my_history[round_num - 1];
        }
    }
    
    my_history[round_num] = move;
    return move;
}

void read_bot_move(char bot_move) {
    bot_history[round_num] = bot_move;
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
