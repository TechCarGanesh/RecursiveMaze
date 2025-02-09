# Name: Ganesh Kumar
# Date: 02/09/2025
# Instructor: Professor Andres Calle
# Project Information: In this lab, you will implement a recursive algorithm to solve a maze.
# The maze is represented as a 2D array where 1 represents walls and 0 represents valid paths.
# The goal is to find a path from the starting point to the exit, if one exists, using recursion.
def isInsideMaze(array, row, col):
    # If the columns are less, then we are to the left of the starting point
    # and if columns is greater than n columns then we are to the right of the columns in the array.
    if((col >= 0 and col <= len(array[0]) - 1) and
            # If row is less than 0, then we are outside the maze.
            # If row is greater than the number of rows, then we are outside the maze.
            (row >= 0 and row <= len(array) - 1)) and (array[row][col] != 1):
        return True
    else:
        return False
def recursive_maze_function(array, row, col):
    # Base Case is when you have reached the end.
    # Check the base condition it should check if we reached the end of the maze.
    # End of the maze is row == nrows - 1
    # and col == ncols - 1 assuming your array is 0 to nrows - 1 and 0 to ncols - 1.
    if(row == len(array) - 1 and col == len(array[0]) - 1):
        if (array[row][col] == 0):
            print("Exiting the maze successfully.")
            array[row][col] = 2
            return True
        else:
            print("Stuck in the maze: row: ", row, "col: ", col)
            return False

    # After the base condition check if you are not moving out of the array boundaries.
    # Remember array boundaries are row >= 0 and <= nrows - 1 and col >= 0 and <= ncols - 1
    if(isInsideMaze(array, row, col)):

        # If step 2 is true then you are inside the maze,
        # so check if you are on array which has a 0 in it,
        # then make it a 2 or 3 or whatever you want to mark it with
        if(array[row][col] == 0):
            array[row][col] = 2
        else:
            return False

        # Now the recursive steps begin. Since you are starting from the top left row = 0 and col = 0.
        # You should move down.
        # To move down make row = row+1 keep the col same and call recursive_maze function pass the same parameters.
        # Check if recursive_maze function returns a true and return true
        if(recursive_maze_function(array, row + 1, col)):
            return True

        # If step 4 is fase, it means you ran into an obstacle time to move right, left or back up one row.
        # To back up one row row = row - 1 and call recursive_maze again
        # and check if recursive_maze function return true and return true.
        if (recursive_maze_function(array, row - 1, col)):
            return True

        # Repeat step 5 for moving right col = col + 1 keep row same
        if (recursive_maze_function(array, row, col + 1)):
            return True

        # Repeat the step 6 for moving left col = col - 1 keep row same
        if (recursive_maze_function(array, row, col - 1)):
            return True
    # else:
    #     # If 4 - 7 fails time to back up and return
    #     print("Backing up")
    #     return False

    # If all steps fail, then return false.
    return False

def main():
    maze_array = [
        [0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 1, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 0, 0],
    ]

    for rows in maze_array:
        print(rows)
    row = 0
    col = 0
    recursive_maze_function(maze_array, row, col)
    for rows in maze_array:
        print(rows)


if __name__=="__main__":
    main()
# Result 1:
# C:\Users\pkuma\AppData\Local\Microsoft\WindowsApps\python3.11.exe C:\Users\pkuma\OneDrive\Desktop\MISC\DEANZA_FALL\PYTHON\PYTHON_FALL2024\recursion.py
# [0, 0, 0, 1, 0]
# [1, 0, 0, 1, 0]
# [1, 1, 0, 1, 0]
# [0, 1, 0, 0, 1]
# [1, 1, 1, 0, 1]
# [1, 1, 1, 0, 0]
# Exiting the maze successfully.
# [2, 2, 0, 1, 0]
# [1, 2, 2, 1, 0]
# [1, 1, 2, 1, 0]
# [0, 1, 2, 2, 1]
# [1, 1, 1, 2, 1]
# [1, 1, 1, 2, 2]
#
# Process finished with exit code 0
# Result 2:
# C:\Users\pkuma\AppData\Local\Microsoft\WindowsApps\python3.11.exe C:\Users\pkuma\OneDrive\Desktop\MISC\DEANZA_FALL\PYTHON\PYTHON_FALL2024\recursion.py
# [0, 0, 0, 1, 0]
# [1, 0, 0, 1, 0]
# [1, 1, 0, 1, 0]
# [0, 1, 0, 0, 1]
# [1, 1, 1, 0, 1]
# [1, 1, 1, 0, 1]
# Stuck in the maze: row:  5 col:  4
# [2, 2, 2, 1, 0]
# [1, 2, 2, 1, 0]
# [1, 1, 2, 1, 0]
# [0, 1, 2, 2, 1]
# [1, 1, 1, 2, 1]
# [1, 1, 1, 2, 1]
#
# Process finished with exit code 0