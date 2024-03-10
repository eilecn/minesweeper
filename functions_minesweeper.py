def initialise_board():
    """
    Initialises the Minesweeper board

    Returns:
        board (list): The initialised board
    """

    board = ["O"] * 25
    return board


def display_board(board):
    """
    Displays the board to the user

    Arguments:
    board (list): The initialised board

    """
    for index in range(len(board)):
        # Hiding all the mines from the player
        if board[index] == "X":
            board[index] = "O"

    print(board[0:5])
    print(board[5:10])
    print(board[10:15])
    print(board[15:20])
    print(board[20:25])
    return


def insert_mines(board, positions):
    """
    Inserts the mines into the board.

    Arguments:
        board (list): The initialised board
        positions (list of lists of int): A list of lists containing the coordinates for each mine's position on the board.

    Returns:
        board (list): The board with mines inserted.

    Preconditions:
        Inputted integers in list of lists for argument positions must be between 0 and 4 inclusive.
    """
    n = len(positions)
    counter = 0
    for pos in range(0, n):
        if counter < n:
            row = positions[counter][0]
            col = positions[counter][1]
            spot = (row * 5) + col
            board[spot] = "X"
            counter = counter + 1
            if counter == n:
                break
    return board


def count_adjacent_mines(board, row, col):
    """
    Counts the number of adjacent mines (excluding diagonals) to any given position in the 5x5 board.

    Arguments:
         board (list): The board with mines inserted.
         row (int): The row of the position to search adjacent mines.
         col (int): The column of the position to search adjacent mines.

    Returns:
        number(int): The number of adjacent mines to the specified position

    """
    number = 0
    # Checking if there is a mine above
    if row != 0:
        if board[(row*5) + col - 5] == "X":
            number += 1

    # Checking if there is a mine below
    if row != 4:
        if board[(row*5) + col + 5] == "X":
            number += 1

    # Checking if there is a mine on the left
    if col != 0:
        if board[(row*5) + col - 1] == "X":
            number += 1

    # Checking if there is a mine on the right
    if col != 4:
        if board[(row*5) + col + 1] == "X":
            number += 1

    return number


def play_turn(board, row, column):
    """
    Determines whether the inputted position uncovers a mine or is adjacent to a mine or neither.

    Arguments:
        board (list): The board with mines inserted.
        row (int): The row of the position to search for a mine.
        column (int): The column of the position to search for a mine.

    Returns:
        board (list): The updated board displaying a "#" if a mine has been found, a " " if there are no adjacent mines
        or a number string if there is an adjacent mine present.
        result (bool): A boolean value indicating if a mine has been found.

    Preconditions:
        Inputted integers for arguments row and column must be between 0 and 4 inclusive.
    """
    if board[(row*5+column)] in [" ", "1", "2", "3", "4"]:
        # If player chooses a position that has already been uncovered
        result = False
        print("Position has already been uncovered!")

    if board[(row*5+column)] == "X":
        # If player uncovers a mine
        result = True
        board[row*5+column] = "#"

    if board[(row * 5 + column)] == "O":
        # If player doesn't uncover a mine
        result = False
        if count_adjacent_mines(board, row, column) == 0:
            board[row * 5 + column] = " "
        if count_adjacent_mines(board, row, column) != 0:
            board[row * 5 + column] = str(count_adjacent_mines(board, row, column))
            return board, result


def check_win(board):
    """
    Determines whether the player has won by clearing all the spaces without a mine

    Arguments:
        board (list): The board with mines inserted after turns from the player.

    Returns:
        True or False (bool): A boolean value indicating whether the player has won or not.


    """
    for index in range(len(board)):
        if board[index] == "O":
            return False
    return True


def play_game(positions):
    """
    Allows the player to play the game of Minesweeper by taking user input and playing turns.

    Arguments:
        positions (list of lists of int): The positions of each mine on the board

    Preconditions:
        Inputted integers in list of lists for argument positions must be between 0 and 4 inclusive.
    """
    board = initialise_board()
    board = insert_mines(board, positions)
    y = 0
    while not check_win(board) and y == 0:
        display_board(board)
        userinput = input("Enter row and column (eg: 0 2 for row 0 and column 2): ")
        userinputlist = userinput.split(" ")
        # If player doesn't follow correct format for input
        if len(userinputlist) != 2:
            print("Invalid input!")
            continue
        if userinputlist[0] not in ["0", "1", "2", "3", "4"]:
            print("Input is out of range!")
            continue
        if userinputlist[1] not in ["0", "1", "2", "3", "4"]:
            print("Input is out of range!")
            continue
        board = insert_mines(board, positions)
        play_turn(board, int(userinputlist[0]), int(userinputlist[1]))
        for index in range(len(board)):
            if board[index] == "#":
                print("You lose :(")
                display_board(board)
                y = 1
                break
            elif check_win(board):
                print("You win! :)")
                display_board(board)
                y = 1
                break
    return
