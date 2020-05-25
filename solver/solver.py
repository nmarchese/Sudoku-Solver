from time import time
from collections import OrderedDict

hard_board = [
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
expert_board = [
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
wrong_board = [
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
board_len = 9

def print_board(board):
  """Pretty print board with dividing lines and empty cells (0) converted to a blank space"""
  print()
  print("    0 1 2   3 4 5   6 7 8")
  print("   -----------------------")
  for i in range(board_len):
    if i != 0 and i % 3 == 0:
      # print dividing line every 3 rows
      print("  |-------+-------+-------|")
    print(i, "|", end=" ")
    for j in range(board_len):
      if j != 0 and j % 3 == 0:
        # print divider every 3 cells
        print("| ", end="")
      print(board[i][j] if board[i][j] != 0 else " ", end=" ")
    print("|",i, end="")
    print()
  print("   -----------------------")
  print("    0 1 2   3 4 5   6 7 8")
  print()

def solve_timed(board, solve_method, timer):
  """Solve board using given solve_method and record ammount of time taken to complete"""
  start_time = time()
  solved = solve_method(board)
  finish_time = time()
  timer.append(finish_time - start_time)
  return solved

def solve(board):
  """Solve board using basic backtracking algorithm"""
  next = find_next_empty(board)
  if next:
    # try all numbers for next position
    for num in range(1,10):
      if check_valid(num, next, board):
        # number is valid, set to position
        board[next[0]][next[1]] = num
        # recursive call to solve next position
        if solve(board):
          return True

        # couldn't find valid number for next position
        # backtrack
        board[next[0]][next[1]] = 0
    
    # board unsolvable
    return False
  else:
    # every position filled, board solved
    return True

def solve_with_note_sorting_start(board):
  """Make initial call to recursive method with a new notes dict from get_notes_dict"""
  return solve_with_note_sorting(board, get_notes_dict(board))

def solve_with_note_sorting(board, notes_dict):
  """
  solve board using backtracking algorithm that goes through sorted positions
  starting from the position with the fewest possible options
  """

  # get item with fewest notes in notes_dict
  next = get_pos_with_fewest_notes(notes_dict)

  if next:
    # try each number in next position's notes
    for num in notes_dict[next]:
      board[next[0]][next[1]] = num
      if remove_notes(num, next, notes_dict):
        # notes_dict remains valid
        # recursive call to solve next position
        if solve_with_note_sorting(board, notes_dict):
          return True
        
      # notes_dict made invaled by move
      # backtrack
      board[next[0]][next[1]] = 0
      add_notes(next, notes_dict, board)

    # board unsolvable
    return False
  else:
    # no more notes, all positions filled
    return True

def find_next_empty(board):
  """Finds the next empty cell each row, left to right, top to bottom"""
  for y in range(board_len):
    for x in range(board_len):
      if not board[y][x]:
        return (y, x)

  return None

def check_valid(num, pos, board):
  """Check if number (num) provided for position (pos) is a valid/legal sudoko move"""
  y_pos = pos[0]
  x_pos = pos[1]

  # check row amd column:
  for xy in range(board_len):
    if num == board[y_pos][xy]:
      return False
    if num == board[xy][x_pos]:
      return False
  
  # check box:
  y_box_root = y_pos - (y_pos % 3)
  x_box_root = x_pos - (x_pos % 3)
  for y in range(y_box_root, y_box_root + 3):
    for x in range(x_box_root, x_box_root + 3):
      if num == board[y][x]:
        return False

  return True

def get_notes(pos, board):
  """get list of all posible valid numbers for given position (pos) and board"""
  notes = []
  if not board[pos[0]][pos[1]]:
    for num in range(1,10):
      if check_valid(num, pos, board):
        notes.append(num)
  
  return notes
    
def get_notes_dict(board):
  """get dict of notes for every empty coordinate on board (position : notes_list)"""
  notes_dict = {}
  for y in range(board_len):
    for x in range(board_len):
      pos = (y,x)
      notes_dict[pos] = get_notes(pos, board)
  
  return notes_dict

def remove_notes(num, pos, notes_dict):
  """
  Remove number (num) from notes in notes_dict for each position in the given
  position's (pos) row, column, and box
  """

  y_pos = pos[0]
  x_pos = pos[1]
  
  # remove notes for pos
  notes_dict[pos] = []

  # remove notes for num in row and column
  for xy in range(board_len):
    y_pos_notes = notes_dict[(y_pos, xy)]
    x_pos_notes = notes_dict[(xy, x_pos)]
    if x_pos_notes.count(num):
      # num exists in pos' notes, remove it
      x_pos_notes.remove(num)
      if not x_pos_notes:
        # no notes remain for unfilled pos, notes_dict no longer valid
        return False
    if y_pos_notes.count(num):
      # num exists in pos' notes, remove it
      y_pos_notes.remove(num)
      if not y_pos_notes:
        # no notes remain for unfilled pos, notes_dict no longer valid
        return False

  # remove notes for num in box
  y_box_root = y_pos - (y_pos % 3)
  x_box_root = x_pos - (x_pos % 3)
  for y in range(y_box_root, y_box_root + 3):
    for x in range(x_box_root, x_box_root + 3):
      pos_notes = notes_dict[(y, x)]
      if pos_notes.count(num):
        # num exists in pos' notes, remove it
        pos_notes.remove(num)
        if not pos_notes:
          # no notes remain for unfilled pos, notes_dict no longer valid
          return False
  
  # removed all notes and all effected positions still have at least one note
  return True

def add_notes(pos, notes_dict, board):
  """
  Add notes back (get new list of correct notes based on current board) for
  every position in the provided position's (pos) row, column, and box
  """

  y_pos = pos[0]
  x_pos = pos[1]
  
  # add notes for pos
  notes_dict[pos] = get_notes(pos, board)

  # add notes for pos row and column
  for xy in range(board_len):
    if not board[y_pos][xy]:
      # position on board is empty, add notes
      notes_dict[(y_pos, xy)] = get_notes((y_pos, xy), board)
    if not board[xy][x_pos]:
      # position on board is empty, add notes
      notes_dict[(xy, x_pos)] = get_notes((xy, x_pos), board)
  
  # add notes for pos box
  y_box_root = y_pos - (y_pos % 3)
  x_box_root = x_pos - (x_pos % 3)
  for y in range(y_box_root, y_box_root + 3):
    for x in range(x_box_root, x_box_root + 3):
      if not board[y][x]:
        # position on board is empty, add notes
        notes_dict[(y, x)] = get_notes((y, x), board)

def get_pos_with_fewest_notes(notes_dict):
  """Get the position with the fewest current notes"""
  # sort notes_dict fewest notes to most notes
  ordered_notes_dict = OrderedDict(sorted(notes_dict.items(), key=lambda t: len(t[1])))
  for pos in ordered_notes_dict:
    # only return first position that has non-empty notes list
    if ordered_notes_dict[pos]:
      return pos
  # no notes remain
  return None

def run(board):
  """ Run both solve methods with a timer using provided board"""

  print()
  print("Solving provided Sudoku board:")
  print_board(board)

  print()
  print("Solving board with basic backtracking solve method:")
  board_1 = [row[:] for row in board]
  timer_1 = []
  if solve_timed(board_1, solve, timer_1):
    print_board(board_1)
  else:
    print("*** Couldn't find a solution ***")
  print("Finished in:", *timer_1)

  print()

  print("Solving board with notes driven backtracking solve method:")
  board_2 = [row[:] for row in board]
  timer_2 = []
  if solve_timed(board_2, solve_with_note_sorting_start, timer_2):
    print_board(board_2)
  else:
    print("*** Couldn't find a solution ***")
  print("Finished in:", *timer_2)

  print()
  if board_1 == board_2:
    print("Notes driven solve method was", "%.2f" % (timer_1[0] / timer_2[0]), "times faster")
  else:
    print("Solve methods found different solutions...")

  print()

if __name__ == '__main__':
  run(wrong_board)
  run(hard_board)
  run(expert_board) 