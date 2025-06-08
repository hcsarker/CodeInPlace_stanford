"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
     # Solves labyrinth.
    while front_is_clear():  # Move until there is nowhere to go (see what find_direction() does!)
        move_to_wall()
        find_direction()

def find_direction():
    """
    Turns Karel to the unblocked direction, if an unblocked direction exists. 
    If both left and right are blocked, Karel will not turn.
    
    Pre: There is a wall in front of Karel.
    Post: Karel has turned into an unblocked direction if one exists.
    """

    if left_is_clear():
        turn_left()
    if right_is_clear():
        turn_right()

def turn_right():
    for i in range(3):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()