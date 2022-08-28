#include <iostream>

using namespace std;

/**
 * Determine what move to play this round of rock paper scissors and return it
 */
char play_move() {
    // YOUR CODE HERE
    return ' ';
}

/**
 * Read in the opponent's move for this round of rock paper scissors
 * 
 * bot_move: the move made by the bot
 */
void read_bot_move(char bot_move) {
    // YOUR CODE HERE
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
