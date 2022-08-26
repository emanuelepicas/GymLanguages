final_list = []
def load_words():
    print ("Loading word list from file ...\n\n")
    inFile = open("wordlist")
    line = inFile.readlines()
    for words in line:
         final_list.append(words.replace("\n",""))
    return final_list

