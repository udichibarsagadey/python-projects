import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}"))
        if guess < random_number:
            print("sorry! Too low ")
        elif guess > random_number:
            print("sorry! Too high ")
            
    print(f"yay! Congo you have guessed the number {random_number} correctly")
        
def coumputer_guess(x):
    low = 1
    high = x
    feedback = " "
    while feedback != 'c'and low != high:
        guess = random.randint(low,high)
        feedback = input(f"Is {guess} Too high (H), Too low (L) or correct (c)").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1 
        
print(f'yay! the coumputer have gussed your number {guess} correctly ')
        
guess(100)