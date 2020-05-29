import unittest
import time

from solver import solver

board_len = 9
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
test_board_solved_incorrect = [
  [1, 6, 5, 1, 4, 7, 3, 2, 8], 
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
test_board_expert_not_started = [
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
test_board_expert_solved = [
  [1, 6, 4, 2, 5, 8, 3, 9, 7],
  [8, 9, 7, 4, 1, 3, 6, 5, 2],
  [2, 3, 5, 9, 6, 7, 4, 8, 1],
  [7, 4, 1, 5, 3, 6, 8, 2, 9],
  [5, 8, 3, 1, 9, 2, 7, 4, 6],
  [6, 2, 9, 7, 8, 4, 5, 1, 3],
  [9, 7, 2, 3, 4, 5, 1, 6, 8],
  [4, 1, 6, 8, 7, 9, 2, 3, 5],
  [3, 5, 8, 6, 2, 1, 9, 7, 4]
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
test_board_basic_two_solutions = [
  [0, 0, 3, 4, 5, 6, 7, 8, 9],
  [4, 5, 6, 7, 8, 9, 1, 2, 3],
  [7, 8, 9, 1, 2, 3, 4, 5, 6],
  [0, 0, 4, 3, 6, 5, 8, 9, 7],
  [3, 6, 5, 8, 9, 7, 2, 1, 4],
  [8, 9, 7, 2, 1, 4, 3, 6, 5],
  [5, 3, 1, 6, 4, 2, 9, 7, 8],
  [6, 4, 2, 9, 7, 8, 5, 3, 1],
  [9, 7, 8, 5, 3, 1, 6, 4, 2]
]
test_board_basic_complete_one = [
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [4, 5, 6, 7, 8, 9, 1, 2, 3],
  [7, 8, 9, 1, 2, 3, 4, 5, 6],
  [2, 1, 4, 3, 6, 5, 8, 9, 7],
  [3, 6, 5, 8, 9, 7, 2, 1, 4],
  [8, 9, 7, 2, 1, 4, 3, 6, 5],
  [5, 3, 1, 6, 4, 2, 9, 7, 8],
  [6, 4, 2, 9, 7, 8, 5, 3, 1],
  [9, 7, 8, 5, 3, 1, 6, 4, 2]
]
test_board_basic_complete_two = [
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [4, 5, 6, 7, 8, 9, 1, 2, 3],
  [7, 8, 9, 1, 2, 3, 4, 5, 6],
  [2, 1, 4, 3, 6, 5, 8, 9, 7],
  [3, 6, 5, 8, 9, 7, 2, 1, 4],
  [8, 9, 7, 2, 1, 4, 3, 6, 5],
  [5, 3, 1, 6, 4, 2, 9, 7, 8],
  [6, 4, 2, 9, 7, 8, 5, 3, 1],
  [9, 7, 8, 5, 3, 1, 6, 4, 2]
]
test_board_basic_removed_cells = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1, 2, 3],
  [0, 0, 0, 1, 2, 3, 4, 5, 6],
  [0, 1, 0, 0, 0, 5, 0, 0, 7],
  [0, 0, 5, 0, 0, 7, 2, 0, 0],
  [0, 0, 7, 2, 0, 0, 3, 6, 0],
  [0, 0, 0, 0, 0, 0, 0, 7, 8],
  [0, 4, 2, 0, 7, 8, 5, 0, 0],
  [0, 7, 8, 5, 0, 0, 6, 0, 0]
]
ordered_cells_list = [
  (0,0),
  (0,1),
  (0,2),
  (0,3),
  (0,4),
  (0,5),
  (0,6),
  (0,7),
  (0,8),
  (1,0),
  (1,1),
  (1,2),
  (1,3),
  (1,4),
  (1,5),
  (1,6),
  (1,7),
  (1,8),
  (2,0),
  (2,1),
  (2,2),
  (2,3),
  (2,4),
  (2,5),
  (2,6),
  (2,7),
  (2,8),
  (3,0),
  (3,1),
  (3,2),
  (3,3),
  (3,4),
  (3,5),
  (3,6),
  (3,7),
  (3,8),
  (4,0),
  (4,1),
  (4,2),
  (4,3),
  (4,4),
  (4,5),
  (4,6),
  (4,7),
  (4,8),
  (5,0),
  (5,1),
  (5,2),
  (5,3),
  (5,4),
  (5,5),
  (5,6),
  (5,7),
  (5,8),
  (6,0),
  (6,1),
  (6,2),
  (6,3),
  (6,4),
  (6,5),
  (6,6),
  (6,7),
  (6,8),
  (7,0),
  (7,1),
  (7,2),
  (7,3),
  (7,4),
  (7,5),
  (7,6),
  (7,7),
  (7,8),
  (8,0),
  (8,1),
  (8,2),
  (8,3),
  (8,4),
  (8,5),
  (8,6),
  (8,7),
  (8,8),
]
test_board_not_started_notes_dict = {
  (0,0): [2,4,5,9],
  (0,1): [4,5,6],
  (0,2): [5,6],
  (0,3): [],
  (0,4): [4,6,8],
  (0,5): [],
  (0,6): [],
  (0,7): [2,4,5,6,9],
  (0,8): [2,4,5,8,9],
  (1,0): [2,4,7,9],
  (1,1): [3,4,6,7],
  (1,2): [],
  (1,3): [4,6,8],
  (1,4): [3,4,6,8],
  (1,5): [],
  (1,6): [2,6,8],
  (1,7): [2,4,6,9],
  (1,8): [2,4,8,9],
  (2,0): [],
  (2,1): [3,4,5,6],
  (2,2): [3,5,6],
  (2,3): [],
  (2,4): [],
  (2,5): [3,4,6],
  (2,6): [1,5,6],
  (2,7): [],
  (2,8): [4,5],
  (3,0): [],
  (3,1): [],
  (3,2): [5,7,8],
  (3,3): [5,8,9],
  (3,4): [3,7,8],
  (3,5): [3],
  (3,6): [],
  (3,7): [3,5,9],
  (3,8): [],
  (4,0): [1,5],
  (4,1): [1,5,8],
  (4,2): [],
  (4,3): [4,5,6,8],
  (4,4): [1,2,3,4,6,8],
  (4,5): [1,2,3,4,6],
  (4,6): [],
  (4,7): [2,3,5],
  (4,8): [2,5],
  (5,0): [],
  (5,1): [1,5,7],
  (5,2): [],
  (5,3): [5,9],
  (5,4): [1,2,7],
  (5,5): [1,2],
  (5,6): [2,5],
  (5,7): [],
  (5,8): [],
  (6,0): [1,4,7],
  (6,1): [],
  (6,2): [6,7],
  (6,3): [4,6],
  (6,4): [],
  (6,5): [],
  (6,6): [1,2,6],
  (6,7): [1,2,4,6],
  (6,8): [],
  (7,0): [1,4,5,7],
  (7,1): [1,4,5,6,7,8],
  (7,2): [5,6,7,8],
  (7,3): [],
  (7,4): [1,2,4,6],
  (7,5): [1,2,4,6],
  (7,6): [],
  (7,7): [1,2,4,5,6],
  (7,8): [2,4,5,7,8],
  (8,0): [1,4,5],
  (8,1): [1,3,4,5,6,8],
  (8,2): [],
  (8,3): [],
  (8,4): [1,4,6],
  (8,5): [],
  (8,6): [1,5,6,8],
  (8,7): [1,4,5,6],
  (8,8): [4,5,8],
}
test_board_not_started_notes_dict_after_first_move = {
  (0,0): [2,4,5,9],
  (0,1): [4,5,6],
  (0,2): [5,6],
  (0,3): [],
  (0,4): [4,6,8],
  (0,5): [],
  (0,6): [],
  (0,7): [2,4,5,6,9],
  (0,8): [2,4,5,8,9],
  (1,0): [2,4,7,9],
  (1,1): [3,4,6,7],
  (1,2): [],
  (1,3): [4,6,8],
  (1,4): [3,4,6,8],
  (1,5): [],
  (1,6): [2,6,8],
  (1,7): [2,4,6,9],
  (1,8): [2,4,8,9],
  (2,0): [],
  (2,1): [3,4,5,6],
  (2,2): [3,5,6],
  (2,3): [],
  (2,4): [],
  (2,5): [4,6],
  (2,6): [1,5,6],
  (2,7): [],
  (2,8): [4,5],
  (3,0): [],
  (3,1): [],
  (3,2): [5,7,8],
  (3,3): [5,8,9],
  (3,4): [7,8],
  (3,5): [],
  (3,6): [],
  (3,7): [5,9],
  (3,8): [],
  (4,0): [1,5],
  (4,1): [1,5,8],
  (4,2): [],
  (4,3): [4,5,6,8],
  (4,4): [1,2,4,6,8],
  (4,5): [1,2,4,6],
  (4,6): [],
  (4,7): [2,3,5],
  (4,8): [2,5],
  (5,0): [],
  (5,1): [1,5,7],
  (5,2): [],
  (5,3): [5,9],
  (5,4): [1,2,7],
  (5,5): [1,2],
  (5,6): [2,5],
  (5,7): [],
  (5,8): [],
  (6,0): [1,4,7],
  (6,1): [],
  (6,2): [6,7],
  (6,3): [4,6],
  (6,4): [],
  (6,5): [],
  (6,6): [1,2,6],
  (6,7): [1,2,4,6],
  (6,8): [],
  (7,0): [1,4,5,7],
  (7,1): [1,4,5,6,7,8],
  (7,2): [5,6,7,8],
  (7,3): [],
  (7,4): [1,2,4,6],
  (7,5): [1,2,4,6],
  (7,6): [],
  (7,7): [1,2,4,5,6],
  (7,8): [2,4,5,7,8],
  (8,0): [1,4,5],
  (8,1): [1,3,4,5,6,8],
  (8,2): [],
  (8,3): [],
  (8,4): [1,4,6],
  (8,5): [],
  (8,6): [1,5,6,8],
  (8,7): [1,4,5,6],
  (8,8): [4,5,8],
}

class TestSolver(unittest.TestCase):
  def test_find_next_empty(self):
    """
    Test that it finds the next empty cell
    """
    board = [row[:] for row in test_board_partial_complete_1]
    result = solver.find_next_empty(board)
    expected = (1, 3)
    self.assertEqual(result, expected)

  def test_check_valid_returns_true_when_valid(self):
    """
    Test that check valid returns true when a valid number is
    provided for the given position and current board.
    """
    board = [row[:] for row in test_board_partial_complete_1]
    position = (1, 3)
    number = 6
    result = solver.check_valid(number, position, board)
    self.assertTrue(result)

  def test_check_valid_returns_false_when_invalid_row(self):
    """
    Test that check valid returns false when number provided is
    invalid because same number exists in same row.
    """
    board = [row[:] for row in test_board_not_started]
    position = (0, 0)
    number = 7
    result = solver.check_valid(number, position, board)
    self.assertFalse(result)

  def test_check_valid_returns_false_when_invalid_column(self):
    """
    Test that check valid returns false when number provided is
    invalid because same number exists in same column.
    """
    board = [row[:] for row in test_board_not_started]
    position = (0, 0)
    number = 6
    result = solver.check_valid(number, position, board)
    self.assertFalse(result)

  def test_check_valid_returns_false_when_invalid_box(self):
    """
    Test that check valid returns false when number provided is
    invalid because same number exists in same box.
    """
    board = [row[:] for row in test_board_partial_complete_2]
    position = (0, 1)
    number = 8
    result = solver.check_valid(number, position, board)
    self.assertFalse(result)

  def test_solve_returns_true_and_completes_board(self):
    """
    Test that solve returns true and modifies board to correct
    completed status when a solvable board is provided.
    """
    board = [row[:] for row in test_board_not_started]
    result = solver.solve(board)
    self.assertTrue(result)
    self.assertEqual(board, test_board_solved)

  def test_solve_returns_true_and_completes__expert_board(self):
    """
    Test that solve returns true and modifies board to correct
    completed status when a solvable board is provided.
    """
    board = [row[:] for row in test_board_expert_not_started]
    result = solver.solve(board)
    self.assertTrue(result)
    self.assertEqual(board, test_board_expert_solved)

  def test_solve_returns_false_for_unsolvable_board(self):
    """
    Test that solve returns false and when an unsolvable
    board is provided.
    """
    board = [row[:] for row in test_board_unsolvable]
    result = solver.solve(board)
    self.assertFalse(result)

  def test_get_notes_returns_correct_notes(self):
    """
    Test that get_notes returns a list of all posible/valid
    numbers for the given position and board
    """
    board = [row[:] for row in test_board_not_started]
    pos = (0, 0)
    result = solver.get_notes(pos, board)
    expected = [2, 4, 5, 9]
    self.assertEqual(result, expected)

  def test_get_notes_returns_empty_list_for_completed_pos(self):
    """
    Test that get_notes returns an empty list when position is
    already filled
    """
    board = [row[:] for row in test_board_not_started]
    pos = (0, 3)
    result = solver.get_notes(pos, board)
    expected = []
    self.assertEqual(result, expected)

  def test_get_notes_dict_returns_correct_notes_for_all_pos(self):
    """
    Test that get_notes_dict returns dictionary of all positions
    to notes with each notes list containing correct notes
    """
    board = [row[:] for row in test_board_not_started]
    result = solver.get_notes_dict(board)
    expected = test_board_not_started_notes_dict
    self.assertEqual(result, expected)

  def test_remove_notes_removes_notes_correctly(self):
    """
    Test that remove_notes removes all notes for position (pos)
    and removes the notes for the number (num) provided in that
    position's row, column, and box
    """
    notes_dict = test_board_not_started_notes_dict.copy()
    num = 3
    y_pos = 3
    x_pos = 5
    bool_result = solver.remove_notes(num, (y_pos, x_pos), notes_dict)
    expected = test_board_not_started_notes_dict_after_first_move
    self.assertTrue(bool_result)
    self.assertEqual(notes_dict, expected)

  def test_remove_notes_returns_false_when_resulting_in_invalid_notes(self):
    """
    Test that remove_notes returns false when the removal of notes results
    in an un-filled position being left with no notes. i.e. remove_notes
    removes the last note from a position other than the position passed in
    """
    notes_dict = test_board_not_started_notes_dict.copy()
    num = 3
    y_pos = 3
    x_pos = 4
    bool_result = solver.remove_notes(num, (y_pos, x_pos), notes_dict)
    self.assertFalse(bool_result)

  def test_add_notes_adds_notes_back_correctly(self):
    """
    Test that add_notes adds all notes back to position (pos)
    and adds number (num) to notes lists for that position's
    row, column, and box
    """
    notes_dict = test_board_not_started_notes_dict_after_first_move.copy()
    y_pos = 3
    x_pos = 5
    solver.add_notes((y_pos, x_pos), notes_dict, test_board_not_started)
    expected = test_board_not_started_notes_dict
    self.assertEqual(notes_dict, expected)

  def test_solve_with_note_sorting_returns_true_and_completes_board(self):
    """
    Test that solve_with_note_sorting returns true and modifies board
    to correct completed status when a solvable board is provided.
    """
    board = [row[:] for row in test_board_not_started]
    result = solver.solve_with_note_sorting(board)
    self.assertTrue(result)
    self.assertEqual(board, test_board_solved)

  def test_solve_with_note_sorting_returns_true_and_completes_expert_board(self):
    """
    Test that solve_with_note_sorting returns true and modifies board
    to correct completed status when a solvable board is provided.
    """
    board = [row[:] for row in test_board_expert_not_started]
    result = solver.solve_with_note_sorting(board)
    self.assertTrue(result)
    self.assertEqual(board, test_board_expert_solved)

  def test_solve_with_note_sorting_returns_false_for_unsolvable_board(self):
    """
    Test that solve_with_note_sorting returns false and when an
    unsolvable board is provided.
    """
    board = [row[:] for row in test_board_unsolvable]
    result = solver.solve_with_note_sorting(board)
    self.assertFalse(result)

  def test_call_timed_accurately_records_time(self):
    """
    Test that solve_timed accurately records time taken to run
    provided solve method
    """
    board = None
    def mock_solve(board):
      time.sleep(.01)
    timer = []
    solver.call_timed(mock_solve, timer, board)
    expected = .01
    self.assertEqual("%.2f" % timer[0], "%.2f" % expected)

  def test_check_board_valid_returns_true_for_valid_board(self):
    """
    Test that check_board_valid returns True when board provided is complete and valid
    """
    result = solver.check_board_valid(test_board_solved)
    self.assertTrue(result)

  def test_check_board_valid_returns_false_for_non_valid_board(self):
    """
    Test that check_board_valid returns False when board provided is not valid
    """
    result = solver.check_board_valid(test_board_solved_incorrect)
    self.assertFalse(result)

  def test_check_board_valid_returns_false_for_incomplete_board(self):
    """
    Test that check_board_valid returns False when board provided is not complete
    """
    result = solver.check_board_valid(test_board_not_started)
    self.assertFalse(result)

  def test_generate_cells_fills_board_with_valid_numbers(self):
    """
    Test that generate_cells fills an empty board and resulting board is valid
    """
    board = [[0 for x in range(board_len)] for y in range(board_len)]
    solver.generate_cells(board)
    result = solver.check_board_valid(board)
    self.assertTrue(result)

  def test_get_random_cells_list_returns_81_randomized_unique_cells(self):
    """
    Test that get_random_cells returns a list of 81 unique cells in a random order
    """
    result = solver.get_random_cells_list()
    self.assertTrue(len(result) == 81)
    self.assertNotEqual(result, ordered_cells_list)
    for cell in ordered_cells_list:
      self.assertTrue(result.count(cell) == 1)
  
  def test_check_if_multiple_solutions_returns_true_when_multiple_solutions_exist(self):
    """
    Test that check_if_multiple_solutions returns True when a board with more than one
    possible solution is provided
    """
    board = [row[:] for row in test_board_basic_two_solutions]
    result = solver.check_if_multiple_solutions(board)
    self.assertTrue(result)

  def test_check_if_multiple_solutions_returns_false_when_only_one_solution_exists(self):
    """
    Test that check_if_multiple_solutions returns False when a board with only one
    possible solution is provided
    """
    board = [row[:] for row in test_board_not_started]
    result = solver.check_if_multiple_solutions(board)
    self.assertFalse(result)

  def test_find_all_solutions_results_in_solutions_list_containing_all_possible_solutions(self):
    """
    Test that find_all_solutions results in provided solutions list containing all possible solutions
    to provided board
    """
    solutions = []
    board = [row[:] for row in test_board_basic_two_solutions]
    solver.find_all_solutions(board, solutions)
    self.assertEqual(len(solutions), 2)
    self.assertTrue(solutions.count(test_board_basic_complete_one) == 1)
    self.assertTrue(solutions.count(test_board_basic_complete_two) == 1)


  def test_remove_numbers_results_in_partially_empty_board_with_one_solution(self):
    """
    Test that remove_numbers results in provided board partially empty in a
    configuaration that allows for only one solution
    """
    board = [row[:] for row in test_board_basic_complete_one]
    solver.remove_numbers(board, ordered_cells_list)
    self.assertEqual(board, test_board_basic_removed_cells)
  
if __name__ == '__main__':
  unittest.main()