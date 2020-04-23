import random
import os

def find_Word(value,user_progress, answer):
    index = 0
    while index < len(user_progress):
        index = answer.find(value, index)
        if index == -1:
            break
        user_progress[index] = value
        index += 1
    return user_progress

def read_file():
    f = open('Words.txt', 'r')
    lines = f.readlines()
    f.close()
    return random.choice(lines)

    
  
def play_game():
    read_file()
    print("Hello Welcome to Toms hang man game! \nThe purpose is to refamiliarize myself with python.\n")
    input("...Please press Enter to start the game...\n")
    answer = read_file()
    user_progress = ['_'] * len(answer)
    letters_guessed = []
    correct = False
    guess_count = 10
    
    while correct == False and guess_count > 0:
        print("The word has been generated and has",len(answer),"letters. You have", guess_count,'guesses.\n' )
        print("so far you have:", user_progress)
        value = input("Type a letter to guess and press enter:\n").lower()
        if value in answer and len(value)==1:
            print("Congrats!",value,"is in the word\n")
            user_progress = find_Word(value, user_progress, answer)
            if "".join(user_progress) == answer:
                correct = True
        else:
            print("Sorry but",value,"wasn't a letter")
        letters_guessed.append(value)
        print("These are the letters you have guessed", letters_guessed)
        guess_count -= 1
        
    if correct == True:
        print("\nYou win the answer was", answer)
    else:
        print("You Lose")
        
        

play_game()
