from termcolor import colored, cprint
import os
import random
import time

O = 'O'
X = 'X'

def clr():
    os.system('clear')
    # os.system('cls')

def display():
    global pos

    clr()
    print("\n\t ",end="")
    for index, p in enumerate(pos):
        if index in [2,5,8]:
            pos_print(p,end="\n\t")
            if index == 8:
                print()
            else:
                print("───┼───┼─── ", end="\n\t ")
            
        else: 
            pos_print(p,end=" │ ")


def pos_print(p,end):
    if type(p) == int:
        cprint(p,"grey",end=end)
    else:
        cprint(p,"yellow",end=end)

def play(turn):
    global av_pos
    turn_sym = O if turn == 0 else X
    choice = -1
    if( ( turn_sym == p1_symbol ) or mode == 2 ):
        if mode == 2:
            print(turn_sym,"turn...")
        else:
            print("Player turn...")
            
        while choice not in av_pos:
            print("Available positions:",av_pos)
            cprint('Choose a position','yellow',end=':')
            choice = int(input())
        
        pos[pos.index(choice)] = turn_sym
        display()
    else:
        computersturn = "Computer's turn..."
        for i in computersturn:
            print(i,end='',flush=True)
            time.sleep(0.1)
        print()
        choice = random.choice(av_pos)
        pos[pos.index(choice)] = turn_sym
        display()
        


def check_status():
    global pos, turn
    turn_sym = O if turn == 0 else X

    # WIN STATUS
    if ( (pos[0] == pos[1] == pos[2] == turn_sym) or \
         (pos[3] == pos[4] == pos[5] == turn_sym) or \
         (pos[6] == pos[7] == pos[8] == turn_sym) or \
         (pos[0] == pos[3] == pos[6] == turn_sym) or \
         (pos[1] == pos[4] == pos[7] == turn_sym) or \
         (pos[2] == pos[5] == pos[8] == turn_sym) or \
         (pos[0] == pos[4] == pos[8] == turn_sym) or \
         (pos[6] == pos[4] == pos[2] == turn_sym) ):
        
        display()
        if (turn_sym == p1_symbol):
            print( "\t  🎉🎉🎉")
            player1won_msg = "    PLAYER1 WON! 🥳"
            for i in player1won_msg:
                cprint(i,'green',end='',flush=True)
                time.sleep(0.1)
            return 1
        elif (mode == 2):
            print( "\t  🎉🎉🎉")
            player2won_msg = "    PLAYER2 WON! 🥳"
            for i in player2won_msg:
                cprint(i,'green',end='',flush=True)
                time.sleep(0.1)
            return 2
        else:
            youlost_msg = "    Sorry, You Lost 😔 "
            for i in youlost_msg:
                cprint(i,'red',end='',flush=True)
                time.sleep(0.1)
            return 2

    # FULL STATUS
    elif (len( av_pos ) == 0):
        cprint( "  🟨 DRAW | The Board is full ", 'yellow')
        return 3

    else:
        return 0


while 1:
    
    pos = [7,8,9, 4,5,6, 1,2,3]

    '''
    Modes:
        1: with computer
        2: with player2
    '''
    mode = -1 

    '''
    Player 1 symbol:
        X: X
        O: O
    '''
    p1_symbol = -1

    '''
    Turn:
        0(False) = Its O turn
        1(True) = Its X turn
    '''
    turn = 0 # start with O
    game_status = 0 # 0 = running, 1 = P1 Won, 2 = P2 Won, 3 = Full/Draw

    clr()
    cprint(" OX Welcome to tic-tac-toe XO", 'cyan')
    
    while mode not in [1,2]:
        cprint("\nYou can either play against a friend or a computer, Who do you want to play against?",'yellow')
        mode = int(input("  [1] Computer  \n  [2] PLAYER2 \n  Choose [1 or 2]: ") or 1)

    print()
    while p1_symbol not in [X,O]:
        cprint("Which symbol would you like? ( O starts first )",'yellow')
        p1_symbol = input("  Choose [O or X]: ")
        p1_symbol = O if p1_symbol in ['o','O', '1', ''] else p1_symbol
        p1_symbol = X if p1_symbol in ['x','X', '0'] else p1_symbol
    
    display()
    av_pos = pos
    while game_status == 0:
        play(turn)
        av_pos = [x for x in pos if type(x) == int] # available positions
        game_status = check_status()
        turn = not turn # switch player

    restart = -1
    cprint("\n\nRestart the game?",'yellow')
    while(restart not in [1,2]):
        restart = int(input("  [1] Yes \n  [2] No \n  Choose [1 or 2]:"))
    if restart == 2:
        break
