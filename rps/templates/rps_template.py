def play_move() -> str:
    '''
    Determine what move to play this round of rock paper scissors and return it
    '''
    # YOUR CODE HERE
    return ' '
        
def read_bot_move(bot_move: str) -> None:
    '''
    Read in the opponent's move for this round of rock paper scissors
    
    bot_move: the move made by the bot
    '''
    # YOUR CODE HERE
    return

def main():
    T = int(input())
    for _ in range(T):
        print(play_move(), flush=True)
        read_bot_move(input())

if __name__ == '__main__':
    main()
