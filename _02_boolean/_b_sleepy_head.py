"""
Use boolean variables to control program logic between two different code
paths.
"""

from tkinter import messagebox
import turtle
if __name__ == '__main__':
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    isWeekend = True
    if isWeekend:
        print("YAY! IT IS THE WEEKEND!")
    else:
        print("IT IS TIME FOR MADDOX TO SAY THAT IT IS THE WEEKEND!")

    pass_exam = True
    if pass_exam:
        print("GOOD JOB, MISTER!")
    else:
        print("YOU ARE BAD!")

    game_over = True
    if game_over:
        print("GAME OVER!")
    Bob = turtle.Turtle()
    red_color = True
    square = True
    if red_color and square:
        Bob.color('red')
        for i in range(4):
            Bob.forward(50)
            Bob.left(90)



