#!/usr/bin/python3

from os import system, name

PLAYERS = 2
DIGITS = 4

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


def plist_init(plist):
    for i in range(PLAYERS):
        plist.append("")
    return plist

def take_input_and_validate(i,mode=0,att=0):
    valid_in = 1;
    if(mode == 1):
        mode_str = "Guess"
        attempt = "Attempt #" + str(att);
    else:
        mode_str = "Secret"
        attempt = ""

    while(valid_in):
        p_set = input("Player " + str(i) + " : Enter your 4-digit " + mode_str + " number " + attempt + ":\t")
        p_set_str = str(p_set)
        if(p_set_str.isnumeric() and (len(p_set_str) == 4) ):
            valid_in = 0
        else:
            print("Entry is not 4-digit numeric -> " + p_set_str)
    if(mode == 0):
        clear()
    return(p_set)


def get_inputs():
    p_num = []
    p_num_str = []

    for i in range(PLAYERS): 
        p_in = take_input_and_validate(i+1)
        p_num.append(p_in)
    return(p_num)


def check(secret,guess):
    sec_str = str(secret)
    gs_str = str(guess)
    #pos_mat_str = str(abs(sec_str-gs_str))
    match = 0
    pos_match = 0
    for i in range(DIGITS):
        for j in range(DIGITS):
            if(gs_str[i] == sec_str[j]):
                match = match + 1
        if(gs_str[i] == sec_str[i]):
            pos_match = pos_match + 1
    print("Matches :" + str(match) + " Position Match : " + str(pos_match))
    return(match,pos_match)
    

def check_score_board(p_tries,p_win):
    if((p_win[0] == 1) or (p_win[1] == 1)):
        for i in range(PLAYERS):
            if((p_win[i] == 1)):
                if((p_win[1-i] == 0) and (p_tries[1-i] >= p_tries[i])):
                    print("Player # " + str(i+1) + " Won the Game!!")
                    exit()
                elif((p_win[1-i] == 0) and (p_tries[1-i] < p_tries[i])):
                    return
                else:
                    print("Match tied!!!")
                    exit()


def start_guessing(p_sec):
    game_on = 1
    p_tries = []
    p_win = []
    for i in range(PLAYERS):
        p_tries.append(0)
        p_win.append(0)

    while(game_on):
        for i in range(PLAYERS):
            p_choice = take_input_and_validate(i+1,1,p_tries[i]+1)
            match,pos_match = check(p_sec[1-i],p_choice) 
            p_tries[i] = p_tries[i] + 1
            if((match == 4) and (pos_match == 4)):
                print("Player #" + str(i+1) + " has guessed the number correctly : " + str(p_sec[1-i]))
                p_win[i] = 1
        check_score_board(p_tries,p_win)
    return
        

if __name__ == '__main__':
    p_sec = get_inputs()
    start_guessing(p_sec)

    
 
