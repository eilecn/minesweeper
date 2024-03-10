import pytest

from functions_minesweeper import *


def test_insert_mines():
    board = initialise_board()
    positions = [[0, 0], [1, 1], [2, 2]]  # Mines at (0,0), (1,1), (2,2)
    board = insert_mines(board, positions)
    assert board[0] == "X"
    assert board[6] == "X"
    assert board[12] == "X"


def test_count_adjacent_mines():
    board = initialise_board()
    positions = [[0, 1], [1, 0], [1, 1]]  # Mines at (0,1), (1,0), (1,1)
    board = insert_mines(board, positions)
    assert count_adjacent_mines(board, 0, 0) == 3
    assert count_adjacent_mines(board, 0, 1) == 2
    assert count_adjacent_mines(board, 1, 1) == 2


def test_play_turn():
    board = initialise_board()
    positions = [[0, 1]]  # Mine at (0,1)
    board = insert_mines(board, positions)
    # Testing uncovering a cell with adjacent mines
    board, result = play_turn(board, 1, 1)
    assert result is False
    assert board[6] == "1"
    # Testing uncovering a mine
    board, result = play_turn(board, 0, 1)
    assert result is True
    assert board[1] == "#"


def test_check_win():
    # Test when all non-mine spaces have been uncovered
    board = ["X"] * 25
    assert check_win(board) is True
    board = ["1"] * 25
    assert check_win(board) is True

    # Test when there are spaces left to uncover
    board = ["1"] * 24 + ["O"]  # One space left to uncover
    assert check_win(board) is False
    board = ["O"] * 25  # All spaces need to be uncovered
    assert check_win(board) is False

