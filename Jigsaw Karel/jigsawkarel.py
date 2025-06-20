from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
   move()
   move()
   pick_beeper()
   move()
   turn_left()
   move()
   move()
   put_beeper()
   turn_left()
   turn_left()
   while front_is_clear():
    move()
   turn_right()
   while front_is_clear():
    move()
   turn_around()



## Turn right function
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
## Turn around function
def turn_around():
    turn_left()
    turn_left()




# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()