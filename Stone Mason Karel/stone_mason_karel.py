from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_right()
    for i in range(4):
        move()
    turn_right()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_left()
    for i in range(4):
        move()
    turn_left()
    for i in range(5):
        put_beeper()
        move()
    for i in range(4):
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_left()

 #turn right   
def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()