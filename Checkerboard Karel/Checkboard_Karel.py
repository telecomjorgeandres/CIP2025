from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""
def main():
    # Step 1: Fill the first column with beepers
    tag_all_rows()

    # Step 2: Fill the first row with a checker pattern
    tag_row()

    # Step 3: Continue filling all rows in a checkerboard pattern
    while left_is_clear():
        turn_left()  # Move up to the next row
        move()
        turn_right()  # Get ready to move horizontally
        tag_row()

    # Final positioning to complete the task
    turn_right()
    move_to_wall()
    turn_left()

# Step 1: Fill the entire first column with beepers, alternating spaces
def tag_all_rows():
    turn_left()  # Face North to begin filling the column
    put_beeper()  # Place a beeper at the starting position
    while front_is_clear():
        move()
        if front_is_clear():  # Skip one space, then place a beeper
            move()
            put_beeper()
    
    turn_around()  # Head back down to position Karel for the next step
    move_to_wall()
    turn_left()  # Face East to begin row placement

# Step 2: Create a checker pattern for a single row
def tag_row():
    if beepers_present():  # If the first square has a beeper, follow the alternating pattern
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()
    else:  # If no beeper is present, adjust the start position
        while front_is_clear():
            move()
            put_beeper()
            if front_is_clear():
                move()

    # Step 3: Position Karel correctly for the next row
    turn_around()
    move_to_wall()
    turn_around()

# Helper function: Turns Karel around
def turn_around():
    turn_left()
    turn_left()

# Helper function: Turns Karel right
def turn_right():
    for i in range(3):
        turn_left()

# Helper function: Moves Karel to the closest wall
def move_to_wall():
    while front_is_clear():
        move()
