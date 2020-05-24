# Sudoku Solver

Python application for solving Sudoku puzzles

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

### Using Different Sudoku Boards

Open solver.py in an editor. The current project has three boards built in, two which are solvable and one which is not. You can view each board where they are difined at the top of the file.

To change which board is used when the project is run, simply change the board that is passed in to the *run()* method at the bottom of the file under the line `if __name__ == '__main__':`.

To run with a custom board you can alter an existing board or add a new one (making sure to follow the structure defined by the example boards).
