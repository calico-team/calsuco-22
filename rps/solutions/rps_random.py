import random

# Solutions should be deterministic, so we need to set our random seed
random.seed(1337)

def play_move() -> str:
    return random.choice('RPS')

def read_bot_move(bot_move: str) -> None:
    # This strategy doesn't care about opponent moves, so we do nothing here
    return

def main():
    T = int(input())
    for _ in range(T):
        print(play_move())
        read_bot_move(input())

if __name__ == '__main__':
    main()
