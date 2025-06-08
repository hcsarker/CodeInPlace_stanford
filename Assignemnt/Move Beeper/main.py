"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
    """
    get_beeper() # Move to beeper and pick it up
    move_up() # Move up 2 rows
    put_beeper() # Put beeper down
    move() # End in top right corner

def get_beeper():
    """ Karel starts facing East in the bottom left of the world and ends having picked up the beeper, one spot forwards. """
    move()
    pick_beeper()

def move_up():
    """ Karel starts facing East in row 1 and ends facing East in row 3. """
    turn_left()  # Face North
    move()  # Move to row 2
    move()  # Move to row 3
    turn_right()  # Face East

def turn_right():
    turn_left()
    turn_left()
    turn_left()
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()