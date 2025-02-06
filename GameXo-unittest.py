import unittest
from GameXO import check_winner

class TestCheckWinner(unittest.TestCase):

    def test_winning_row(self):
        board = [
            ["X", "X", "X"],
            ["O", " ", "O"],
            [" ", " ", " "]
        ]
        self.assertTrue(check_winner(board, "X"))

    def test_winning_column(self):
        board = [
            ["X", "O", " "],
            ["X", "O", " "],
            ["X", " ", " "]
        ]
        self.assertTrue(check_winner(board, "X"))

    def test_winning_diagonal(self):
        board = [
            ["X", "O", " "],
            ["O", "X", " "],
            [" ", " ", "X"]
        ]
        self.assertTrue(check_winner(board, "X"))

    def test_no_winner(self):
        board = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]
        ]
        self.assertFalse(check_winner(board, "X"))
        self.assertFalse(check_winner(board, "O"))

if __name__ == '__main__':
    unittest.main()