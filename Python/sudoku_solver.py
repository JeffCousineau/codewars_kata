from copy import copy, deepcopy
import codewars_test as Test

# Check if there's error in the current puzzle
# return : False is there's no error, True if there's error
def check_for_errors(puzzle):
    # Check horizontal lines
    for i in puzzle: 
        if not only_unique(i):
            return True

    # Check vertical lines
    for i in range(0,9):
        vert_line = []
        for j in range(0,9):
            vert_line.append(puzzle[j][i])
        if not only_unique(vert_line):
            return True

    # Check boxes
    for i in range (0,3):
        for j in range (0,3):
            box = [puzzle[i*3][j*3],puzzle[i*3][j*3+1],puzzle[i*3][j*3+2],puzzle[i*3+1][j*3],puzzle[i*3+1][j*3+1],puzzle[i*3+1][j*3+2],puzzle[i*3+2][j*3],puzzle[i*3+2][j*3+1],puzzle[i*3+2][j*3+2]]
            if not only_unique(box):
                return True 

    return False

# Check if only unique number in line except for the zeros
# return : bool
def only_unique(puzzle_line):
    unique = []
    for i in puzzle_line:
        if i not in unique and not i == 0:
            unique.append(i)
    return True if puzzle_line.count(0)+len(unique) == 9 else False 

# Always give the initial puzzle as an input
# zero_values is the new value for each zero (1D array, line by line)
def fill_new_values(init_puzzle, zero_values):
    new_puzzle = deepcopy(init_puzzle)
    zeros_puzzle = sum(x.count(0) for x in init_puzzle)
    if not len(zero_values) == zeros_puzzle:
        print("NOT THE SAME")
        return init_puzzle
    else:
        it = 0
        for i in range(0,9):
            for j in range(0,9):
                if new_puzzle[i][j] == 0:
                    new_puzzle[i][j] = zero_values[it]
                    it += 1
    return new_puzzle

def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    solved = False

    it = 0
    zero_values = []

    zero_count = sum(x.count(0) for x in puzzle)
    for i in range(0, zero_count):
        zero_values.append(0)
    print(zero_values)
    test_puzzle = []
    while not solved:
        
        # Bruteforce algorithm
        # Go to first 0, put 1, check for error, if no error, next 0, if error, put 2...
        # When at the next 0, if 9 values are tested and there's an error, go back to last 0 and increment

        # Iterate on zero_values array
        zero_values[it] += 1

        # Fill the sudoku with new values
        test_puzzle = fill_new_values(puzzle,zero_values)

        # Check if there's errors in the sudoku
        if check_for_errors(test_puzzle):
            # If 9 is reach, set value to 0 and go back until the value isn't 9
            if zero_values[it] >= 9 :
                while zero_values[it] == 9:
                    zero_values[it] = 0
                    it -= 1

        # If there's no error, check if there's still 0 or else, increment the iterator
        else:
            if not sum(x.count(0) for x in test_puzzle) > 0:
                solved = True
            else :
                it += 1
    
    return test_puzzle


Test.describe('Sudoku')

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

Test.it('Puzzle 1')
Test.assert_equals(sudoku(puzzle), solution, "Incorrect solution for the following puzzle: " + str(puzzle))
