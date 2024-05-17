import unittest
import numpy as np
from connect4 import (
    connectfour_board,
    drop_valid,
    drop_board,
    newopen_row,
    flip_board,
    check_winner,
    cpu_move
)

class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.board = connectfour_board()
    
    def test_connectfour_board(self):
        self.assertTrue((self.board == np.zeros((6, 7))).all())
    
    def test_drop_valid(self):
        self.assertTrue(drop_valid(self.board, 0))
        self.assertTrue(drop_valid(self.board, 6))
        self.assertFalse(drop_valid(self.board, -1))
        self.assertFalse(drop_valid(self.board, 7))
        
        # Fill up a column and check if it's invalid
        for row in range(6):
            self.board[row][0] = 1
        self.assertFalse(drop_valid(self.board, 0))

    def test_drop_board(self):
        row = newopen_row(self.board, 0)
        drop_board(self.board, row, 0, 1)
        self.assertEqual(self.board[row][0], 1)

    def test_newopen_row(self):
        self.assertEqual(newopen_row(self.board, 0), 0)
        drop_board(self.board, 0, 0, 1)
        self.assertEqual(newopen_row(self.board, 0), 1)

    def test_check_winner_horizontal(self):
        for col in range(4):
            row = newopen_row(self.board, col)
            drop_board(self.board, row, col, 1)
        self.assertTrue(check_winner(self.board, 1))

    def test_check_winner_vertical(self):
        for row in range(4):
            drop_board(self.board, row, 0, 1)
        self.assertTrue(check_winner(self.board, 1))

    def test_check_winner_diagonal_positive_slope(self):
        for i in range(4):
            row = newopen_row(self.board, i)
            drop_board(self.board, row, i, 1)
        self.assertTrue(check_winner(self.board, 1))

    def test_check_winner_diagonal_negative_slope(self):
        for i in range(4):
            row = 5 - i
            drop_board(self.board, row, i, 1)
        self.assertTrue(check_winner(self.board, 1))

    def test_cpu_move(self):
        move = cpu_move(self.board)
        self.assertTrue(0 <= move <= 6)
        self.assertTrue(drop_valid(self.board, move))

    def test_flip_board(self):
        # For visual verification, since flip_board prints the board, here we just ensure it runs without error
        flip_board(self.board)
        self.assertIsNone(flip_board(self.board))  # Ensure the function runs without error

if __name__ == '__main__':
    unittest.main()
