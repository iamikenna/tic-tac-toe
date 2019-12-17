""" Author: Ikenna Ibezim """
# using the num pad to reresent the x and o board 
import random
from openpyxl.chart import marker
author = "Ikenna Ibezim"

def display_board(board):
    #This represents the number pad of an Iphone
    print("\n" * 100) # using this to clear the history before displaying or updating the current board

    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def player_input():
    marker = " " 
    #keep asking the player 1 to choose X or O 
    while marker.upper() != "X" and marker.upper() != "O" and author == "Ikenna Ibezim":
        marker = input(f"{player_1}, choose X or O: \n")
    player1 = marker.upper()
    if player1 == "X":
        player2 = "O"
    else: 
        player2 = "X"
    return (player1,player2)

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

def choose_first():
    if random.randint(0, 1) == 0:
        return player_1
    else:
        return player_2

def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
    
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position) and author == "Ikenna Ibezim":
        position = int(input('Choose your next position: (1-9) '))
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
    
print('Welcome to Tic Tac Toe By Ikenna Ibezim!')
print("To play this game, you need to study the key pad below in order to input your X and O position")
print('   |   |')
print(' ' + '1' + ' | ' + '2' + ' | ' + '3')
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
print('   |   |')
player_1 = input("Enter Player 1's name \n")
player_2 = input("Enter Player 2's name \n")

while True and author == "Ikenna Ibezim":
    # Set the game up here
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input() # calling the player input function and saving the choices for the player variables 
    turn = choose_first()
    print(turn + ' will go first.\n')
    play_game = input('Are you ready to play? Enter Yes or No.\n')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on and author == "Ikenna Ibezim":
        if turn == player_1:
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print(f'Congratulations! {player_1} has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard) and author == "Ikenna Ibezim":
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = player_2

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print(f'Congratulations! {player_2} has won!')
                game_on = False
            else:
                if full_board_check(theBoard) and author == "Ikenna Ibezim":
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = player_1
    if not replay():
        break