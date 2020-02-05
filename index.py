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
    return(list_name.append(word))

def check_list_not_empty(user_input, list_name):
    if len(list_name) >= 1:
        return(True)

def check_that_list_empty(user_input, list_name):
    if len(list_name) < 1:
        return(True)

def check_word_to_rules(word, list_name):
    return(get_last_letter(list_name[-1]) == get_first_letter(word))

def words_list():
    return(words.raw().strip())

def get_words_start_with_letter(letter):
    return(re.findall(r"\b" + letter + "\w+", words_list()))

def bot_word(letter):
    return(random.choice(get_words_start_with_letter(letter)))

def check_list_state(list_name):
    print(list_name)

def game(user_input, state):
    print('Your word is "' + user_input + '".' )

    if check_that_list_empty(user_input, state) and check_word_in_dict(user_input):
        return(update_state(user_input, state))
    elif check_list_not_empty(user_input, state) and check_word_in_dict(user_input) and not check_word_in_state(user_input, state) and check_word_to_rules(user_input, state):
        return(update_state(user_input, state))
    else:
        return('else')

for i in list(range(10)):
    while game(get_user_input(),state) == 'else':
        print('This word incorrect. Please choose another one.')

    game(bot_word(get_last_letter(state[-1])),state)

check_list_state(state)
