positions = [ [0, 0],[0, 1],[0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]

def initialise_board():
    board = ["O"] * 25
    return board

def display_board(board):
    for index in range(len(board)):
        if board[index] == "X":
            board[index] = "O"
    print(board[0:5])
    print(board[5:10])
    print(board[10:15])
    print(board[15:20])
    print(board[20:25])
    return

def insert_mines(board, positions):
    noofmines = len(positions)
    counter = 0
    for pos in range (0, noofmines):
        if counter < noofmines:
            row = positions[counter][0]
            col = positions[counter][1]
            spot = (row * 5) + col
            board[spot]= "X"
            counter = counter + 1
            if counter == noofmines:
                break
                return

def count_adjacent_mines(board, row, col):
    number = 0
    #checking above
    if row != 0:
        if board[(row*5) + col - 5] == "X":
            number += 1

    #checking below
    if row != 4:
        if board[(row*5) + col + 5] == "X":
            number += 1

    #checking left
    if col!= 0:
        if board[(row*5) + col - 1] == "X":
            number += 1

    #checking right
    if col!= 4:
        if board[(row*5) + col + 1] == "X":
            number += 1

    return(number)

def play_turn(board, row, column):
    insert_mines(board, positions)
    if board[(row*5+column)] == "X":
        result = True
        board[row*5+column] = "#"

    if board[(row * 5 + column)] == "O":
        result = False
        if count_adjacent_mines(board, row, column) == 0:
            board[row * 5 + column] = " "
        if count_adjacent_mines(board, row, column) != 0:
            board[row * 5 + column] = str(count_adjacent_mines(board, row, column))
            return (board, result)

def check_win(board):
    x = 0
    for index in range(len(board)):
        if board[(index)] == " ":
            x+= 1
            print(board[(index)])
            print(x)
    if x == (25 - len(positions)):
        result = True
    else:
        result = False
    return(result)

def play_game(positions):
    board = initialise_board()
    insert_mines(board, positions)
    y = 0
    while check_win(board) != True and y == 0:
        display_board(board)
        userinput = input("Enter row and column (eg: 1 2 for row 1 and column 2): ")
        userinputlist = userinput.split(" ")
        play_turn(board, int(userinputlist[0]), int(userinputlist[1]))
        for index in range(len(board)):
            if board[index] == "#":
                print("you lose")
                display_board(board)
                y = 1
                break
            elif check_win(board) == True:
                print("you win")
                display_board(board)
                y = 1
                break
    return

