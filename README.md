# Sudoku Solver

Python application for solving Sudoku puzzles.

This application currently contains two different solving methods, one that uses a basic "brute-force" backtracking algorithm and one that uses a similar backtracking algorithm but with a more targeted approach than simply trying every number as it works through the puzzle.
In addition to solving Sudoku puzzles, this application can count the number of possible solutions for a puzzle (although true, valid Sudoku puzzles have only one) and it can generate new Sudoku puzzles from scratch.

Running the solver in its default configuration will generate a new random Sudoku puzzle from scratch, solve the puzzle using both of the solve methods it currently contains, and compare the efficiency of one method vs the other.
A specific customized board can also be used rather than generating a random board. (See [Using Custom Sudoku Boards](#using-custom-sudoku-boards) below)

## Using Sudoku Solver

### Prerequisites

- Python (3.8.3 recomended)

### Running Sudoku Solver

*This will probably change drastically as project evolves (GUI planned for future use)*

For the current state of the project:

Clone or download this repository.

In a comand prompt or terminal, navigate to the project's solver directory

```
>cd C:\path\to\SudokuSolver\solver
```

Run the solver

```
>python solver.py
```

### Running Sudoku Solver's tests

Run python's unittest module from the project root directory

```
>cd C:\path\to\SudokuSolver\
>python -m unittest
```

### Using Custom Sudoku Boards

Open solver.py in an editor. The current project has a default custom board built in, cust_board defined on line 5. In order to use your own custom board, simply modify the values in cust_board while maintaining the defined format. (9 rows with 9 comma seperated 'cell's per row, '0's as empty cells, each cell must contain a single digit number (0-9))

To change use the custom board when the project is run, simply pass the custom board into the *run()* method at the bottom of the file under the line `if __name__ == '__main__':`.