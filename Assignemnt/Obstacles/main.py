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
    # Move to first obstacle
    move()

    # Jump first obstacle
    jump_obstacle()
    put_beeper()
    
    # Jump second obstacle
    jump_obstacle()
    put_beeper()

    # Jump last obstacle
    jump_obstacle()
    put_beeper()

    # Move to last column
    move()
    move()

def jump_obstacle():
    """
    Karel starts facing East, facing a wall.
    Karel ends facing East, on the other side of the wall.
    """
    turn_left() # Face North
    move() # Move up one row
    turn_right() # Face East
    move() # Move forward one column
    turn_right() # Face South
    move() # Move back to bottom row
    turn_left() # Face East

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()