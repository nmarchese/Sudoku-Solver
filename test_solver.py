import unittest

from solver import solver

test_board_not_started = [
  [0, 0, 0, 1, 0, 7, 3, 0, 0],
  [0, 0, 1, 0, 0, 5, 0, 0, 0],
  [8, 0, 0, 2, 9, 0, 0, 7, 0],
  [6, 2, 0, 0, 0, 0, 4, 0, 1],
  [0, 0, 9, 0, 0, 0, 7, 0, 0],
  [3, 0, 4, 0, 0, 0, 0, 8, 6],
  [0, 9, 0, 0, 5, 8, 0, 0, 3],
  [0, 0, 0, 3, 0, 0, 9, 0, 0],
  [0, 0, 2, 7, 0, 9, 0, 0, 0]
]
test_board_solved = [
  [9, 6, 5, 1, 4, 7, 3, 2, 8], 
  [2, 7, 1, 8, 3, 5, 6, 4, 9], 
  [8, 4, 3, 2, 9, 6, 1, 7, 5],
  [6, 2, 7, 5, 8, 3, 4, 9, 1],
  [5, 8, 9, 6, 1, 4, 7, 3, 2],
  [3, 1, 4, 9, 7, 2, 5, 8, 6],
  [7, 9, 6, 4, 5, 8, 2, 1, 3],
  [4, 5, 8, 3, 2, 1, 9, 6, 7],
  [1, 3, 2, 7, 6, 9, 8, 5, 4]
]
test_board_partial_complete_1 = [
  [9, 6, 5, 1, 4, 7, 3, 2, 8],
  [2, 7, 1, 0, 0, 5, 0, 0, 0],
  [8, 0, 0, 2, 9, 0, 0, 7, 0],
  [6, 2, 0, 0, 0, 0, 4, 0, 1],
  [0, 0, 9, 0, 0, 0, 7, 0, 0],
  [3, 0, 4, 0, 0, 0, 0, 8, 6],
  [0, 9, 0, 0, 5, 8, 0, 0, 3],
  [0, 0, 0, 3, 0, 0, 9, 0, 0],
  [0, 0, 2, 7, 0, 9, 0, 0, 0]
]
test_board_partial_complete_2 = [
  [9, 0, 0, 1, 0, 7, 3, 0, 0],
  [0, 0, 1, 0, 0, 5, 0, 0, 0],
  [8, 0, 0, 2, 9, 0, 0, 7, 0],
  [6, 2, 0, 0, 0, 0, 4, 0, 1],
  [0, 0, 9, 0, 0, 0, 7, 0, 0],
  [3, 0, 4, 0, 0, 0, 0, 8, 6],
  [0, 9, 0, 0, 5, 8, 0, 0, 3],
  [0, 0, 0, 3, 0, 0, 9, 0, 0],
  [0, 0, 2, 7, 0, 9, 0, 0, 0]
]
test_board_expert = [
  [0, 0, 0, 0, 0, 0, 3, 0, 7],
  [8, 9, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 6, 7, 4, 0, 1],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 8, 3, 1, 0, 0, 0, 0, 0],
  [6, 0, 0, 0, 0, 4, 5, 0, 0],
  [0, 0, 0, 0, 0, 0, 1, 6, 0],
  [0, 1, 0, 8, 7, 0, 0, 3, 0],
  [3, 5, 0, 0, 2, 0, 0, 0, 0]
]
test_board_unsolvable = [
  [0, 0, 0, 1, 9, 7, 3, 0, 0],
  [0, 0, 1, 0, 0, 5, 0, 0, 0],
  [8, 0, 0, 2, 9, 0, 0, 7, 0],
  [6, 2, 0, 0, 0, 0, 4, 0, 1],
  [0, 0, 9, 0, 0, 0, 7, 0, 0],
  [3, 0, 4, 0, 0, 0, 0, 8, 6],
  [0, 9, 0, 0, 5, 8, 0, 0, 3],
  [0, 0, 0, 3, 0, 0, 9, 0, 0],
  [0, 0, 2, 7, 0, 9, 0, 0, 0]
]

class TestSolver(unittest.TestCase):
  def test_find_next_empty(self):
    """
    Test that it finds the next empty cell
    """
    board = test_board_partial_complete_1
    result = solver.find_next_empty(board)
    self.assertEqual(result, (1, 3))

  def test_check_valid_returns_true_when_valid(self):
    """
    Test that check valid returns true when a valid number is
    provided for the given position and current board.
    """
    board = test_board_partial_complete_1
    position = (1, 3)
    number = 6
    result = solver.check_valid(number, position, board)
    self.assertTrue(result)

  def test_check_valid_returns_false_when_invalid_row(self):
    """
    Test that check valid returns false when number provided is
    invalid because same number exists in same row.
    """
    board = test_board_not_started
    position = (0, 0)
    number = 7
    result = solver.check_valid(number, position, board)
    self.assertFalse(result)

  def test_check_valid_returns_false_when_invalid_column(self):
    """
    Test that check valid returns false when number provided is
    invalid because same number exists in same column.
    """
    board = test_board_not_started
    position = (0, 0)
    number = 6
    result = solver.check_valid(number, position, board)
    self.assertFalse(result)

  def test_check_valid_returns_false_when_invalid_box(self):
    """
    Test that check valid returns false when number provided is
    invalid because same number exists in same box.
    """
    board = test_board_partial_complete_2
    position = (0, 1)
    number = 8
    result = solver.check_valid(number, position, board)
    self.assertFalse(result)

  def test_solve_returns_true_and_completes_board(self):
    """
    Test that solve returns true and modifies board to correct
    completed status when a solvable board is provided.
    """
    board = test_board_not_started
    result = solver.solve(board)
    self.assertTrue(result)
    self.assertEqual(board, test_board_solved)

  def test_solve_returns_false_for_unsolvable_board(self):
    """
    Test that solve returns false and when an unsolvable
    board is provided.
    """
    board = test_board_unsolvable
    result = solver.solve(board)
    self.assertFalse(result)

if __name__ == '__main__':
  unittest.main()