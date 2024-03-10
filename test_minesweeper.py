import pytest
from functions_minesweeper import *


def test_insert_mines_in_corners():
    board = initialise_board()
    positions = [[0, 0], [0, 4], [4, 0], [4, 4]]  # Mines at (0,0), (1,1), (2,2)
    board = insert_mines(board, positions)
    assert board[0] == "X"
    assert board[4] == "X"
    assert board[20] == "X"
    assert board[24] == "X"


def test_count_adjacent_mines_in_corners():
    board = initialise_board()
    positions = [[0, 0], [0, 4], [4, 0], [4, 4], [2, 2]]
    insert_mines(board, positions)
    count = count_adjacent_mines(board, 0, 0)
    assert count == 0
    count = count_adjacent_mines(board, 0, 4)
    assert count == 0
    count = count_adjacent_mines(board, 4, 0)
    assert count == 0
    count = count_adjacent_mines(board, 4, 4)
    assert count == 0
    count = count_adjacent_mines(board, 2, 2)
    assert count == 0
    count = count_adjacent_mines(board, 1, 2)
    assert count == 1
    count = count_adjacent_mines(board, 3, 2)
    assert count == 1
    count = count_adjacent_mines(board, 2, 1)
    assert count == 1
    count = count_adjacent_mines(board, 2, 3)
    assert count == 1


def test_play_turn():
    board = initialise_board()
    positions = [[2, 2]]
    insert_mines(board, positions)
    play_turn(board, 2, 2)
    assert board[12] == "#"

    board = initialise_board()
    positions = [[2, 2]]
    insert_mines(board, positions)
    play_turn(board, 1, 2)
    assert board[7] == "1"

    board = initialise_board()
    positions = [[2, 2]]
    insert_mines(board, positions)
    play_turn(board, 3, 2)
    assert board[17] == "1"

    board = initialise_board()
    positions = [[2, 2]]
    insert_mines(board, positions)
    play_turn(board, 2, 1)
    assert board[11] == "1"

    board = initialise_board()
    positions = [[2, 2]]
    insert_mines(board, positions)
    play_turn(board, 2, 3)
    assert board[13] == "1"

    board = initialise_board()
    positions = [[2, 2]]
    insert_mines(board, positions)
    play_turn(board, 1, 1)
    assert board[6] == " "


def test_check_win():
    board = initialise_board()
    assert check_win(board) is False

    board = initialise_board()
    positions = [[0, 0], [0, 4], [4, 0], [4, 4]]
    insert_mines(board, positions)
    assert check_win(board) is False

    board = [" "] * 25
    assert check_win(board) is True

    board = [" "] * 25
    positions = [[0, 0], [0, 4], [4, 0], [4, 4]]
    insert_mines(board, positions)
    assert check_win(board) is True

    board = [" "] * 25
    positions = [[0, 0], [0, 4], [4, 0]]
    insert_mines(board, positions)
    board[24] = "O"
    assert check_win(board) is False



