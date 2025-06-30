from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    while front_is_clear():
        fill_row()
        return_to_start() # Return to the start of the row
        turn_left()
        if front_is_clear():
            move()
            turn_right()
        else:
            turn_right()
            return_to_start()
            # Don’t fill again—exit naturally
            while front_is_clear():  # Do nothing, just idle
                move()  

def fill_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def return_to_start():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()





    


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()