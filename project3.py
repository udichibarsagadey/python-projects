import random

def play():
    user = input("What's your choice ??'r' for rock 'p' for paper and 's' for scisors")
    coumputer = random.choice(['r','p','s'])
    
    if user == coumputer:
        return 'it is a tie'

    if is_win(user,coumputer):
        return 'you won'

    return 'you lost'
def is_win(player , opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 's'):
        return True
    
    print(play())
