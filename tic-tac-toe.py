

# 1. prepare a 3 x 3 playing field, either imaginary or visually

# define the field in koordinates from (0,0) to (2,2)
# make a library with coordinates
# assign each coordinate another value
grid = {
    "line1": {"0,0": ".", "1,0":".", "2,0":"."},
    "line2": {"0,1": ".", "1,1":".", "2,1":"."},
    "line3": {"0,2": ".", "1,2":".", "2,2":"."},
}

import sys
import random

marker_p = "X"
marker_c = "O"
def move_human():

    #loop till correct input

    while True:
        input_human = input("Input Human: ")

        found = False



    # search for input in nested dict, check if not assigned before
    # and assign "X"(value) to used input,
        for lines in grid.values():
            if input_human in lines:
                if lines[input_human] == ".":
                    found = True
                    lines[input_human] = marker_p
                    break

    #print Grid
        if found:
            for line in ["line1", "line2", "line3"]:
                for coord in grid[line].values():
                    print(coord, end = " " )
                print ()
            break

    #redo task
        else:
            print("Field already used, pick another.")

def move_computer():

    # transform "grid" to list, containing all keys (coordinates)
    # as keys of inner dict cannot be accessed otherwise

    all_coords = [key for line in grid.values() for key, value in line.items() if value == "."]
    # take a random key nad define it the name "move"
    move = random.choice(all_coords)

    print("Computer Input: ", move)
    # search the grid for the key and change the corresponding value to "O"
    for _, inner_dict in grid.items():
        if move in inner_dict:
            inner_dict[move] = marker_c
            break  # stop after updating

    # prints the current grid
    for line in ["line1", "line2", "line3"]:
        for coord in grid[line].values():
            print(coord, end = " " )
        print ()

    #check if value in grid has 3 X in a row (horizantal, vertikal, diagonal)
    #end script and write: Human won

def check():
    for row in grid.values():
        if all(cell == marker_p for cell in row.values()):
            print ("Player Won, Congratulations!")
            sys.exit()
    # column = [["0,0","0,1","0,2"], ["1,0","1,1","1,2"], ["2,0","2,1","2,2"]]
    # for row in column:
        # if all(row[column] == marker_p for row in grid.values()):
            # print ("Player Won, Congratulations!")

#check if 3 "X" in a column
    columns = [
    ["0,0", "0,1", "0,2"],
    ["1,0", "1,1", "1,2"],
    ["2,0", "2,1", "2,2"]
    ]
    # loops through each list (col_key = list1/list2/list3)
    for col_key in columns:

        #grid.values() returns the inner dictionaries, as those are the "values" and the keys are "line1/line2/line3"
        #col_key returns a single list from columns
        #zip() pairs each row with the responding key in the inner dict of grid
        #for row, key in zip(...): loops through each pair, assigning row and key
        #row[key] == marker_p : checks if the value at that coordinate is equal to marker_p ("X" or "O").
        #all(...) → returns True only if every cell in this column equals the marker_p
        if all(row[key] == marker_p for row, key in zip(grid.values(), col_key)):
            print ("Player Won, Congratulations!")
            sys.exit()

#check if 3 "X" in a diagonal
    diagonal = [
        ["0,0", "1,1", "2,2"],
        ["2,0", "1,1", "0,2"]
    ]
    for diag in diagonal:
        if all(grid[key] == marker_p for grid, key in zip(grid.values(), diag)):
            print ("Player Won, Congratulations!")
            sys.exit()


    #check if there are no more values called "."
    #end script and write "Draw"
    is_full = True

    for row in grid.values():
        for cell in row.values():
            if cell == ".":
                is_full = False
                break
        if not is_full:
            break
    if is_full:
        print ("Draw!")
        sys.exit()


#import function



    #check if value in grid has 3 X in a row (horizantal, vertikal, diagonal)
    #end script and write: Human won

#check if 3 "O" in a row
    for row in grid.values():
        if all(cell == marker_c for cell in row.values()):
            print ("Computer Won, Congratulations!")
            sys.exit()

    # column = [["0,0","0,1","0,2"], ["1,0","1,1","1,2"], ["2,0","2,1","2,2"]]
    # for row in column:
        # if all(row[column] == marker_c for row in grid.values()):
            # print ("Player Won, Congratulations!")

#check if 3 "X" in a column
    columns = [
    ["0,0", "0,1", "0,2"],
    ["1,0", "1,1", "1,2"],
    ["2,0", "2,1", "2,2"]
    ]
    # loops through each list (col_key = list1/list2/list3)
    for col_key in columns:

        #grid.values() returns the inner dictionaries, as those are the "values" and the keys are "line1/line2/line3"
        #col_key returns a single list from columns
        #zip() pairs each row with the responding key in the inner dict of grid
        #for row, key in zip(...): loops through each pair, assigning row and key
        #row[key] == marker_c : checks if the value at that coordinate is equal to marker_c ("X" or "O").
        #all(...) → returns True only if every cell in this column equals the marker_c
        if all(row[key] == marker_c for row, key in zip(grid.values(), col_key)):
            print ("Computer Won, Congratulations!")
            sys.exit()

#check if 3 "X" in a diagonal
    diagonal = [
        ["0,0", "1,1", "2,2"],
        ["2,0", "1,1", "0,2"]
    ]
    for diag in diagonal:
        if all(grid[key] == marker_c for grid, key in zip(grid.values(), diag)):
            print ("Computer Won, Congratulations!")
            sys.exit()


# repeat moves till either won or draw and then exit

while True:
    move_human()
    check()
    move_computer()
    check()










