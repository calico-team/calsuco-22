#include <iostream>
#include <stdlib.h>

using namespace std;

char MOVES[] = {'R', 'P', 'S'};

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
        move = MOVES[rand() % 3];
    }
    
    my_history[round_num] = move;
    return move;
}

void read_bot_move(char bot_move) {
    bot_history[round_num] = bot_move;
}

int main() {
    // Solutions should be deterministic, so we need to set our random seed
    srand(1337);
    
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
