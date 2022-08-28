import random

# Solutions should be deterministic, so we need to set our random seed
random.seed(1337)

my_history, bot_history = [], []

def play_move() -> str:
    if len(my_history) >= 2 and my_history[-1] == my_history[-2]:
        if my_history[-1] == 'R':
            move = 'S'
        elif my_history[-1] == 'P':
            move = 'R'
        else:
            move = 'P'
    elif len(bot_history) >= 2 and bot_history[-1] == bot_history[-2]:
        move = bot_history[-1]
    else:
        move = random.choice('RPS')
    
    my_history.append(move)
    return move

def read_bot_move(bot_move: str) -> None:
    bot_history.append(bot_move)

def main():
    T = int(input())
    for _ in range(T):
        print(play_move())
        read_bot_move(input())

if __name__ == '__main__':
    main()
