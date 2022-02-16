def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear(): #We don't have a wall in our right side so we can turn right and move
        turn_right()
        move()
    elif front_is_clear(): #We have a clear path, we move straight ahead
        move()
    else: #if we have a wall on the right and in front, we only have our left clear
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
