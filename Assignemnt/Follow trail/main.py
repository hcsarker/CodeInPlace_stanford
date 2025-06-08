from karel.stanfordkarel import *

def main():
    while beepers_present():
        follow_straight_trail()
        step_backwards()
        # Check left
        turn_left()
        move()
        if no_beepers_present():
            # Trail doesn't continue to the left;
            # Go right
            step_backwards()
            turn_around()
            move()
            # Here the next iteration of the loop will check if there is a beeper; if there is we will keep going and if not we will stop!
    
def follow_straight_trail():
    while beepers_present():
        pick_beeper()
        move()

def step_backwards():
    """
    Turn around and go back one step, 
    then face the same way you were when you started
    """
    turn_around()
    move()
    turn_around()

def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()