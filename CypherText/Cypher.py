#!/usr/bin/python3.9

import string
import textStart

print(textStart.logo)


list_Characters_Lower_Case = string.ascii_lowercase
list_alphabet = []
end_cypher = False

# creating the list of alphabet, the cause of the double run
# of for loop is just to enlarge the number shift selection to 26,
# in order to not cause any error during the shift of letters present at the
# end of the list

for pos, char in enumerate(list_Characters_Lower_Case):
    list_alphabet.append(char)


for pos, char in enumerate(list_Characters_Lower_Case):
    list_alphabet.append(char)


while not end_cypher:

    direction = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt\n")

    if (direction == "encrypt"):
        print('You can only encrypt only lowercase letter, the other charachters will remain the same\n')

    text_to_cypher = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    def encrypt(text, shift_number):
        cypher_text = ""
        for letter in text:
            if letter in list_alphabet:
                current_position = list_alphabet.index(letter)
                new_positiion = current_position + shift_number
                new_letter = list_alphabet[new_positiion]
                cypher_text += new_letter
            else:
                cypher_text += letter
        cypher_text += "$" + str(shift)
        print(f'The encoded text is {cypher_text}\n\n')

    def decrypt(text, shift_number):
        normal_text = ""
        for letter in text:
            if letter in list_alphabet:
                if (letter == "$"):
                    break
                current_position = list_alphabet.index(letter)
                new_positiion = current_position - shift_number
                right_letter = list_alphabet[new_positiion]
                normal_text += right_letter
            else:
                normal_text += letter
        print(f'The decoded text is {normal_text}\n\n')

    if (direction == "encrypt"):
        encrypt(text=text_to_cypher, shift_number=shift)

    if (direction == "decrypt"):
        print("An hint, if you don't remember the shit number insert the number after the $ sign\n\n")
        decrypt(text=text_to_cypher, shift_number=shift)

    restart = input("Type 'y' if you want to go again. Otherwise type 'n'.\n")
    if restart == "n":
        end_cypher = True
        print("Goodbye")
