#Hangman game for Cs dojo Part 1

#Chris Edosomwan Freshman Year CS Student

#4-14-2022

import random 

sports = ("Basketball","Soccer","Baseball","Football","cricket")

word = random.choice(sports)

guessed_correctly = ()

guessed_incorrectly = ()

tries = 4

Hangman_count = -1

while tries > 0:
    output = ""
    for letter in word:
        if letter in guessed_correctly:
            output += letter
        else:
            output += "_"
    if output == word:
        break 
    print("guess the word: ", output)
    
    print(tries,"chances left for game")
    guess = input().lower()
    if guess in guessed_correctly or guess in guessed_incorrectly:
        print=("you already guessed",guess)
    else:
        if guess in word:
            print("Great choice!!YOUR CHOICE WAS CORRECT" )
        else:
            print("Ouu sorry you. Your choice isnt correct.")
            
            Hangman_count = Hangman_count + 1
            tries = tries - 1
           
            print(Hangman_count)
            
if tries > 0:
    print("you guessed it right!!")
else:
    print("my apologies you guessed wrong.Try again")
    
    
                
            