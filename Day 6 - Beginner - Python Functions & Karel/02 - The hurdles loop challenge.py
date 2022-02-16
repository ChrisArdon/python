def turn_right():
    turn_left()
    turn_left()
    turn_left()

def one_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for obstacle in range(6):
    one_jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
