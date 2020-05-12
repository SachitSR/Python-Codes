import random

def disp_board(board): # Prints the current board state
    index =9
    count=1
    while count<=index:
        if count==1 or count==4 or count==7:
            print('| {} '.format(board[count-1]), end="|")
        else:
            print(' {} '.format(board[count-1]), end="|")
        if count%3==0 and count !=9:
            print('\n-------------')
        count+=1




def player_input(num): #Asks the first player for an X/O selection
    while True:
        user=input('Player {} do you want to be X or O ? '.format(num))
        inp = user.upper()
        if inp=='X' or inp=='O':
            return inp
            False
        else:
            print('Wrong input entered. Please enter a X or O')



def map_input(position, board, ip): # entering player action in the board
    if position>=1 and position<=9:
        board[position-1]= ip
    return board


def place_check(board,position):  #Checking board position occupancy
    if board[position-1]==' ':
        return True
    else:
        return False


def player_position():  # Inputs the player's choice of position
    while True:
        try:
            pos = int(input("Enter your desired position: "))
        except:
            print('Not a valid input. Try again')
        else:
            if pos>=1 and pos<=9:
                return pos
                break
            else:
                print("You did not enter a number between 1-9")



def first_player(): # Chooses a random first players
    return (random.randint(1,2))

def board_full(board): #Tie Checker--- Checks if the board is full
    full=0
    for item in board:
        if item==' ':
            full=1
    if full==1:
        return False
    else:
        return True

def replay():
    while True:
        choice = (input('Do you want to play again Y/N ? : ')).upper()
        if choice=='Y':
            return True
            False
        elif choice=='N':
            return False
            False
        else:
            print('Enter a valid input')



def win_check(board,char): ##Checks if a player has won after the current move
    for position in range(1,4):
        if board[position+2]==board[position+5]==board[position-1]==char:
            return True
    for position in range(1,8,3):
        if board[position]==board[position+1]==board[position-1]==char:
            return True
    if (board[0]==board[4]==board[8]==char) or (board[2]==board[4]==board[6]==char):
        return True



############ M A I N ###########
game=True
while game==True:
    turn=0
    win=0
    tie=0
    print(' WELCOME TO TIC TAC TOE!!!! \n The Game board requires you to input your place choices as shown below')
    test_board=[1,2,3,4,5,6,7,8,9]
    disp_board(test_board)
    print('\n\n\nGAME BOARD\n\n')
    game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    disp_board(game_board)
    player = first_player()
    print('\n\nPlayer {} is going First'.format(player))
    player_list = []
    input_list = []
    if player==1:
        player_list=[player,2]
    elif player==2:
        player_list=[player,1]
    pinput=player_input(player)
    if pinput=='X':
        input_list = [pinput,'O']
        print('player {} has been assigned {} and player {} has been assigned {}\n\n'.format(player_list[0],input_list[0], player_list[1],input_list[1]))
    elif pinput=='O':
        input_list = [pinput,'X']
        print('player {} has been assigned {} and player {} has been assigned {}\n\n'.format(player_list[0], input_list[0], player_list[1],input_list[1]))
    while win==0 and tie==0:
        if turn==0: ### First Player turn
            check=True
            print('\nPlayer {} Turn\n'.format(player_list[turn]))
            while check==True:
                player_pos = player_position()
                temp= place_check(game_board,player_pos)
                if temp==True:
                    map_input(player_pos, game_board, input_list[turn])
                    check=False
                else:
                    print('\nThis position is occupied. Try again\n')
            disp_board(game_board)
            if win_check(game_board, input_list[0])==True:
                win=1
            elif board_full(game_board)==True:
                tie=1
            else:
                turn=1
        if turn==1: ### Second Player Turn
            check=True
            print('\nPlayer {} Turn\n'.format(player_list[turn]))
            while check==True:
                player_pos = player_position()
                temp= place_check(game_board,player_pos)
                if temp==True:
                    map_input(player_pos, game_board, input_list[turn])
                    check=False
                else:
                    print('\nThis position is occupied. Try again\n')
            disp_board(game_board)
            if win_check(game_board,input_list[1]) == True:
                win = 1
            elif board_full(game_board) == True:
                tie = 1
            else:
                turn=0
    if win==1:
        print('\n\n\nCongratulations!!!!')
        print('\nplayer {} has won the game\n'.format(player_list[turn]))
    if tie==1:
        print('\n\nThis Game is a tie\n')
    game=replay()
    print('\n'*50)






