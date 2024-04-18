import random


def show_board():
    print("+---+---+---+")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("+---+---+---+")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("+---+---+---+")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("+---+---+---+")


# function to determine the winner
def is_winner(char):
    # horizontal wining conditions
    if board[0] == char and board[1] == char and board[2] == char:
        return True
    elif board[3] == char and board[4] == char and board[5] == char:
        return True
    elif board[6] == char and board[7] == char and board[8] == char:
        return True

    # vertical wining condition
    elif board[0] == char and board[3] == char and board[6] == char:
        return True
    elif board[1] == char and board[4] == char and board[7] == char:
        return True
    elif board[2] == char and board[5] == char and board[8] == char:
        return True

    # diagonal wining condition
    elif board[0] == char and board[4] == char and board[8] == char:
        return True
    elif board[2] == char and board[4] == char and board[6] == char:
        return True
    else:
        return False


# function to determine a tie
def is_full():
    if board.count(' ') == 0:
        return True
    else:
        return False


# choose letter function
def choose_letter():
    letter = ''
    while not (letter == 'X' or letter == "O"):
        print('Do you wish to be X or O?')
        letter = input().upper()
    return letter


# toss for letter function
def toss():
    if random.randint(0, 1) == 0:
        return 'X'
    else:
        return 'O'


# restart game
while True:

    board = [' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' ']

    # calling these 2 functions before showing the board to start game
    if choose_letter() == 'X':
        print('You are X!')
    else:
        print('You are O!')

    # create player list and assign the characters X and O
    player = []
    if toss() == 'X':
        print("X wins toss.")
        player = ['X', 'O']  # initializing the player list
    else:
        player = ['O', 'X']
        print("O wins toss.")

    show_board()

    while True:  # infinite loop to keep the game running
        while True:  # player 1  move
            print(player[0], "\'s turn.", end=' ')
            p1 = int(input('Please enter position on board from (0-9)'))  # ask user for position on board

            if board[p1] == ' ':
                board[p1] = player[0]
                break
            else:
                print('Position is occupied!')
        show_board()  # after player 1 move

        # call is_winner function
        if is_winner(player[0]):
            print(player[0], "wins !!!")
            break  # break out of outer while loop

        # call is_full function
        if is_full():
            print('Its a Tie!')
            break

        while True:  # player 2  move
            print(player[1], "\'s turn.", end=' ')
            p2 = int(input('Please enter position on board from (0-9)'))  # ask user for position on board

            if board[p2] == ' ':
                board[p2] = player[1]
                break
            else:
                print('Position is occupied!')
        show_board()  # after player 2 move

        if is_winner(player[1]):
            print(player[1], "wins !!!")
            break  # break out of outer while loop

        # call is_full function
        if is_full():
            print('Its a Tie!')
            break

    print("Do you wish to continue? (y/n)")
    option = input()
    if option.lower() == 'y':
        continue
    else:
        print("Thank you for playing Tic Tac Toe !!! ")
    break
