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

def print_board(board):
  for i in range(len(board)):
    if i != 0 and i % 3 == 0:
      print("------+-------+------")
    for j in range(len(board[i])):
      if j != 0 and j % 3 == 0:
        print("| ", end="")
      print(board[i][j] if board[i][j] != 0 else " ", end=" ")
    print()

def solve(board):
  next = find_next_empty(board)
  if next:
    # try all numbers for next position
    for num in range(1,10):
      if check_valid(num, next, board):
        board[next[0]][next[1]] = num
        if solve(board):
          return True

        # backtrack
        board[next[0]][next[1]] = 0
    return False
  else:
    return True

def find_next_empty(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 0:
        return (i, j)

  return None

def check_valid(num, pos, board):
  y_pos = pos[0]
  x_pos = pos[1]

  # check row:
  for x in range(len(board[y_pos])):
    if num == board[y_pos][x]:
      return False

  # check column:
  for y in range(len(board)):
    if num == board[y][x_pos]:
      return False
  
  # check box:
  y_box_root = y_pos - (y_pos % 3)
  x_box_root = x_pos - (x_pos % 3)
  for y in range(y_box_root, y_box_root + 3):
    for x in range(x_box_root, x_box_root + 3):
      if num == board[y][x]:
        return False

  return True

def run():
  run_board = hard_board
  if solve(run_board):
    print_board(run_board)
  else:
    print("no solution?")

run()