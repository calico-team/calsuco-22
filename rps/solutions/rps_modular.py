# Variables to track moves
my_history, bot_history = [], []

# Variables to track and crack LCG
lcg_already_cracked = False
bot_rand_history = []
next_bot_move_is_random = False
x, a, c = None, None, None
m = 10 ** 9 + 7
q = []

def play_move() -> str:
    global next_bot_move_is_random, lcg_already_cracked
    
    next_bot_move_is_random = False
    if len(my_history) >= 2 and my_history[-1] == my_history[-2]:
        move = move_that_beats(move_that_beats(my_history[-1]))
    elif len(bot_history) >= 2 and bot_history[-1] == bot_history[-2]:
        move = bot_history[-1]
    else:
        if len(my_history) == 0:
            move = 'R'
        elif lcg_already_cracked:
            move = move_that_beats(get_lcg_move())
        else:
            move = my_history[-1]
        
        next_bot_move_is_random = True

    my_history.append(move)
    return move    

def read_bot_move(bot_move: str) -> None:
    global next_bot_move_is_random, lcg_already_cracked
    
    bot_history.append(bot_move)
    
    if next_bot_move_is_random and not lcg_already_cracked:
        bot_rand_history.append(bot_move)
        
        if len(bot_rand_history) == 19 * 3:
            crack_lcg()
            lcg_already_cracked = True
        
        next_bot_move_is_random = False

def main():
    T = int(input())
    for _ in range(T):
        print(play_move())
        read_bot_move(input())

def move_that_beats(move):
    if move == 'R':
        return 'P'
    elif move == 'P':
        return 'S'
    else:
        return 'R'

def get_lcg_move():
    global x, a, c, m
    
    if not q:
        x = (a * x + c) % m
        temp = x
        for _ in range(19):
            q.append(temp % 3)
            temp //= 3
    move = q[-1]
    q.pop()
    if move == 0:
        return 'R'
    elif move == 1:
        return 'P'
    else:
        return 'S'

def crack_lcg():
    global x, a, c, m
    
    x0, x1, x2 = construct_x(0), construct_x(1), construct_x(2)
    x2_minus_x1 = (x2 - x1) % m
    x1_minus_x0 = (x1 - x0) % m
    
    a = (x2_minus_x1 * modular_inverse(x1_minus_x0, m)) % m
    c = (x1 - x0 * a) % m
    x = x2

def construct_x(index):
    x = 0
    for i in range(19 * index, 19 * (index + 1)):
        x *= 3
        if bot_rand_history[i] == 'R':
            x += 0
        elif bot_rand_history[i] == 'P':
            x += 1
        else:
            x += 2
    return x

# This is due to Euler's/Fermat's Little Theorem
# https://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Using_Euler's_theorem
def modular_inverse(a, m):
    return pow(a, m - 2, m)

if __name__ == '__main__':
    main()
