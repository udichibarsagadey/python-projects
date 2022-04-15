import random
from secrets import choice
from words import words
import string



def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words) 
        
    return word

def hangman():
    lives = 6
    word  = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters =  set()
    
    while len(word_letters) > 0 and lives > 0 :
        print('you have', lives,'lives left and you have used these letters',' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word:',''.join(word_list))
        
        user_letter = input('Guess a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(used_letters)
                
            else:
                lives = lives - 1
                print('the letter in not in the word')
                
        elif user_letter in used_letters:
            print('You have aldready used that charecter. Please try again ')
            
        else:
            print ('Invalid characters. Please try again')
            
    if lives == 0:
        print('sorry you lost. The word was', word)
    else:
        print('Yay! you have guessed the word', word, 'correctly !!')


hangman()