import random
import time

def display_board(board):

    print (" ", board[1] , " | ", board[2], " | ", board[3])
    print ("-----------------")
    print (" ", board[4] , " | ", board[5], " | ", board[6])
    print ("-----------------")
    print (" ", board[7] , " | ", board[8], " | ", board[9])
    
def player_select():
    
    player1 = ''
    player2 = ''
    while True:
        marker = input("Player 1, Select 'X' or 'O': ").upper()
        if marker == 'X' or marker == 'O':
            player1 = marker
            if marker == 'X':
                player2 = 'O'
            else:
                player2 = 'X'
            break
        else:
            print ("Invalid choice, only 'X' and 'O' ")
            continue
            
    return (player1, player2)
    

def place_marker(board, marker, position):
    board[position] = marker
    return board

def win_check(board, mark):
    #Try create empty list & append, win condition = ["x", "x", "x"]
    #Check Horizontal
    if mark == board[1] == board[2] == board[3]:
        return True
    elif mark == board[4] == board[5] == board[6]:
        return True
    elif mark == board[7] == board[8] == board[9]:
        return True
    #Check Vertical
    elif mark == board[1] == board[4] == board[7]:
        return True
    elif mark == board[2] == board[5] == board[8]:
        return True
    elif mark == board[3] == board[6] == board[9]:
        return True
    #Check Diagonal
    elif mark == board[1] == board[5] == board[9]:
        return True
    elif mark == board[3] == board[5] == board[7]:
        return True
    
    return False

def choose_first():
    x = random.randint(1,2)
    print ("Selecting First Player...")
    time.sleep(1)
    return x

def space_check(board, position):
    #empty space = False
    if board[position] == ' ':
        return False
    else:
        return True

def full_board_check(board):
    for i in range(len(board)):
        if space_check(board, i) == False:
            return False
    return True

def player_choice(board):
    while True:
        choice = int(input("Enter Position:"))
        if space_check(board, choice) == False:
            return choice
        
        else:
            print ("Invalid choice, spot taken")
            continue

def replay():
    while True:
        replay = input("Would you like to replay? 'Yes' / 'No': ").lower()
        if replay == 'yes':
            return True
        elif replay == 'no':
            return False
        else:
            print ("Invalid input, 'Yes' or 'No' Only")
            continue
    
#player_select()
#place_marker(test_board,'$',8)
#display_board(test_board)
#win_check(test_board,'X')
#choose_first()
#full_board_check(test_board)
#player_choice(test_board)
#replay()

board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player1 = None
player2 = None
mark = None
position = None

while True:
    player1 , player2 = player_select()

    if choose_first() == 1:
        mark = player1
    else:
        mark = player2
    print ("Player %s Goes First!"%mark)

    display_board(board)

    #Game Loop
    while True:
        position = player_choice(board)
        place_marker(board, mark ,position)
        print('\n'*50)
        display_board(board)
        ##win/draw condition
        if win_check(board, mark) == True:
            print ("Congratulations player ", mark , "WON!")
            break
        elif full_board_check(board) == True:
            print ("DRAW!")
            break
        else:
            if mark == 'X':
                mark = 'O'
            else:
                mark = 'X'
        
        print ('Player %s turn'%mark)
        continue
        

    if replay() == True:
        board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
        continue
    else:
        break

print ("Thank you for playing!")
