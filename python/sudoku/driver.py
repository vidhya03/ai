import sys
from SudokuBoard import *


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python driver.py <input_string> or python driver.py 003020600900305001001806400008102900700000008006708200002609500800203009005010300'
        sys.exit(0)

    sudokuBoard = SudokuBoard(sys.argv[1])
    cspAlgo = SudokuBoardCSPAlgo(sudokuBoard)
    AC3(cspAlgo)

    # Gets assignment from remaining cells
    x = BacktrackingSearch(cspAlgo)

    for var in x:
        cspAlgo.domain[var] = [x[var]]

    sol = ""
    for row in "ABCDEFGHI":
        for col in "123456789":
            sol += str(cspAlgo.domain[row + col][0])

    with open("output.txt", "w") as output:
        output.write(sol)

