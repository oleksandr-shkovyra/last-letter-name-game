import nltk
import re
import random

from nltk.corpus import words

state=[]

def get_user_input():
    return(input('Please, put your word: '))

def get_update_dictionary():
    nltk.download('words')

def get_first_letter(word):
    return(word[0])

def get_last_letter(word):
    return(word[-1])

def check_word_in_dict(word):
    return(word in words.words())

def check_word_in_state(word, list_name):
    return(word in list_name)

def update_state(word, list_name):
    if word not in list_name and check_word_in_dict(word) is True:
        return(list_name.append(word))

def check_list_not_empty(user_input, list_name):
    if len(list_name) >= 1:
        return(True)

def check_that_list_empty(user_input, list_name):
    if len(list_name) < 1:
        return(True)

def check_word_to_rules(word, list_name):
    if str(get_last_letter(list_name[-1])) == str(get_first_letter(word)):
        update_state(word, state)
    else:
        print('Please, choose another word!')

def words_list():
    return(words.raw().strip())

def get_words_start_with_letter(letter, words_list):
    return(re.findall(r"\b" + letter + "\w+", words_list))

def get_random_word(words_list):
    print(random.choice(words_list))

def bot_word(letter):
    get_random_word(get_words_start_with_letter(letter, words_list()))

def check_list_state(list_name):
    print(list_name)

def game(user_input, state):
    if check_word_in_state(user_input, state) is True:
        print('This word in the state!')

    if check_word_in_dict(user_input) is False:
        print("This word not in the dictionary!")

    if check_that_list_empty(user_input, state) is True:
        update_state(user_input, state)

    if check_list_not_empty(user_input, state) is True:
        check_word_to_rules(user_input, state)


#get_update_dictionary()

#for i in list(range(10)):
#    game(get_user_input(),state)
#check_list_state(state)

bot_word('b')
