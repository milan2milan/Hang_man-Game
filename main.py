from hang_man_game import random_word
##########################################################################################################################
def check_game_status(selected_word,current_word_state,attempt_remaining):
    if attempt_remaining <=0:
        print("Sorry you lost 😩 ")
        print("The word was: {}".format(selected_word))
        return False
    if selected_word==current_word_state:
        print("Congratulations !! You Won (\_/)")
        print("                           (*_*)")
        print("                           ( ♥️ )")
        print("                     ✨✨✨✨✨✨✨✨")
        return False
    else:
        return True
###########################################################################################################################
def change_current_word_state(selected_word,input_char,current_word_state):
    modified_word_state=""
    for i in range(len(selected_word)):
        if current_word_state[i]=="_" and selected_word[i]==input_char:
            modified_word_state+=selected_word[i]
        else:
            modified_word_state+=current_word_state[i]
    return modified_word_state   

############################################################################################################################
def input_char_in_word(selected_word,input_char,current_word_state,attempt_remaining):
    if input_char in selected_word:
        current_word_state=change_current_word_state(selected_word,input_char,current_word_state)
        #attempt_remaining-=1
    else:
        attempt_remaining-=1
    return current_word_state,attempt_remaining
####################################################################################   
def print_current_state(current_word_state,attempt_remaining):
    #It will print current status of the game that is the alphabets gussed so far attempts left
    print("Current Word State: ",end=" ")
    for i in current_word_state:
        print(i,end=" ")
    print("\t Attempts Remaining {}".format(attempt_remaining))#which value is provided in peranthisis is insert in currly baces and print with string
################################################################################################################################
def play_game(attempt=5):

    #It will contain main logic of my game 
    selected_word=random_word()#It will store the value of randomly picked word
    #attempts_remaining=attempt
    #It will show present state of the word
    current_word_state = ""
    for i in selected_word:
        if i == ' ' or i == 'a' or i == 'k' or i == 'i' or i == 'c' or i == 'v' or i == 't' or i == 'o' or i == 'I':
            current_word_state += i
            #current_word_state += ""
            continue
        current_word_state += "_"
    attempts_remaining=attempt
    print_current_state(current_word_state,attempts_remaining)
    while True:
        input_char=input("Guess the character: ")
        print("")
        current_word_state,attempts_remaining = input_char_in_word(selected_word,input_char,current_word_state,attempts_remaining)
        print_current_state(current_word_state,attempts_remaining)
        game_end_checker=check_game_status(selected_word,current_word_state,attempts_remaining)
        if game_end_checker==False:
            break
##############################################################################################################################
if __name__=="__main__":
    play_game()