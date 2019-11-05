from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    marker = ' '
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, choose a marker "X" or "O":  ').upper()
    
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')   

def place_marker(board, marker, position):
    
    board[position] = marker

def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))
    
    return position

def replay():
    
    choice = input("Play again? Enter Yes or No: ").lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print (turn + ' will go first')
    
    playGame = input('Ready to play? Y/N: ')
    
    if playGame == 'Y':
        gameOn = True
    else:
        gameOn = False
        
    while gameOn:
        
        if turn == 'Player 1':
            #show the board
            display_board(theBoard)
            #choose a position
            position = player_choice(theBoard)
            #place a marker
            place_marker(theBoard, player1_marker, position)
            #check if won
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Player 1 Wins!')
                gameOn = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Tie game!')
                    break
                else:
                    turn = 'Player 2'        
        
        # Player2's turn.
        if turn == 'Player 2':
            #show the board
            display_board(theBoard)
            #choose a position
            position = player_choice(theBoard)
            #place a marker
            place_marker(theBoard, player2_marker, position)
            #check if won
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 Wins!')
                gameOn = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Tie game!')
                    break
                else:
                    turn = 'Player 1'   
        

    if not replay():
        break