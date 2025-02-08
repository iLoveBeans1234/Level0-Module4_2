"""
Write a program to return the correct letter grade
"""
from tkinter import messagebox, simpledialog, Tk

# The teacher wants you to write a program that converts the score on 2
# 100 point tests to a letter grade. The teacher wants you to average the
# score from the 2 tests and print out the letter grade back to the user.
# The letter grades are assigned as follows:
#   A = 90. to 100
#   B = 79.5 to less than 88.5
#   C = 69.5 to less than 78.5
#   D = 59.5 to less than 68.5
#   F = less than 59.5
if __name__ == '__main__':
    window = Tk()
# Hide the window, hint: use the withdraw method
    window.withdraw()
    # TODO) Ask the user for their score on the FIRST test and store their
    #  score in a variable
    score_1 = simpledialog.askfloat(title="user", prompt="What did you get on your first test?")
    # TODO) Ask the user for their score on the SECOND test and store their
    #  score in a variable
    score_2 = simpledialog.askfloat(title="user", prompt="What did you get on your second test?")
    # TODO) Take the average score of both tests (total score / 2)
    average = (score_1 + score_2) / 2
    # TODO) Use if statements to check the average score and print the
    #  corresponding letter grade back to the user. Also, give a different
    #  message according to their grade. Example, for an 'A' grade:
    #  "Wow! You must have studied really hard for those tests!"
    if average >= 90:
        messagebox.showinfo(title="user", message="GOOD JOB! YOU GOT AN A!")
    elif average >= 80:
        messagebox.showinfo(title="user", message="HEY! YOU ARE SUPPOSED TO GET AN A! NOT A B!")
    elif average >= 70:
        messagebox.showinfo(title="user", message="HOW DID YOU GET A C? YOU NEED TO STUDY HARDER!")
    elif average >= 60:
        messagebox.showinfo(title="user", message="HOW'D YOU GET A D? THAT'S SO BAD! YOU'RE SO DUMB!")
    elif average >= 50:
        messagebox.showinfo(title="user", message="HOW DID YOU GET AN F? WHY ARE YOU SO STUPID?")
