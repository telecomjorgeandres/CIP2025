from karel.stanfordkarel import *


def main():
    ### Step 1: Move to the rightmost position and place a beeper
    while front_is_clear() and no_beepers_present():  
        move()
    put_beeper()  # Mark the right edge of the row
    turn_back()  # Turn around to move back

    ### Step 2: Move to the leftmost position and place another beeper
    while front_is_clear() and no_beepers_present():  
        move()
    put_beeper()  # Mark the left edge of the row
    turn_back()  # Turn around to start narrowing toward the midpoint
    
    ### Step 3: Shrink inward by moving beepers closer
    while no_beepers_present():  
        cycle_A()  # Moves beepers inward one step at a time
    
    ### Step 4: Pick the last beeper to ensure only one remains
    pick_beeper()
    turn_back()  # Turn around after picking up the beeper
    turn_left()  
    turn_left()  

    ### Step 5: Ensure final facing direction
    if facing_west():  # If Karel is facing West, correct orientation
        turn_left()
        turn_left()


### FUNCTIONS:

def turn_back():  
    """ Turns Karel around and moves forward one step """
    turn_left()
    turn_left()
    move()

def cycle_A():  
    """ Moves Karel to the next beeper location, picks it up, and places it closer to the center """
    while front_is_clear() and no_beepers_present():
        move()
    pick_beeper()  # Grab beeper from the current position
    turn_back()  # Move back to shift it closer
    put_beeper()  # Drop the beeper at the new position
    move()  # Advance forward for the next cycle