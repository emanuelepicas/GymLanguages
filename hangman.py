#!/bin/python3.9
import random
import loadWords
import animation
import time

logo = animation.loadLogo()
stages = animation.loadAnimation()
print(len(stages))
print(f'{logo} \n\n\n')
word_list = loadWords.load_words()
time.sleep(2)
end_of_game = False
word_to_guess = random.choice(word_list)
lenght_Word_To_Guess = len(word_to_guess)
lives = 6
letters_used = []
if lives > len(word_to_guess):
    lives = len(word_to_guess)+1
print(
    f'''Welcome to the Hangman Game, you need to guess the wright word chosing the right letters.\nYou will have {lives} lives, every tentative you will loose one of it\n''')


list_name_position = []


for i in range(lenght_Word_To_Guess):
    list_name_position.append("_")


def guess(a):
    for position in range(len(word_to_guess)):
        #print(f'{a} == {word_to_guess[position]}')
        if a == str(word_to_guess[position]):
            print("RIGHT \n\n")
            list_name_position[position] = chosen_word


while not end_of_game:
    #print(word_to_guess)
    print(f'{list_name_position}  \n')
    print(f'Lives avalaible --> {lives} \n')
    chosen_word = input("What is your guess letter ? ")
    chosen_word = str.lower(chosen_word)
    guess(chosen_word)
    if "_" not in list_name_position:
        end_of_game = True
        print("You win!!!")
        time.sleep(2)
        print("Congratulations!!!!!!!!")
    if chosen_word not in word_to_guess:
        lives -= 1
        print('Wrong letter')
        letters_used.append(chosen_word)
        print(stages[lives])
        print(f"Letter used \n {letters_used} \n")
        if lives == 0:
            end_of_game = True
            print("You lost")
            time.sleep(2)
            print(f"The word was {word_to_guess}")