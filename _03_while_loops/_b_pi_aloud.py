"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384
    pi = "3.1415926535897932384"
    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # first digit# second digit
    print(pi[0])
    print(pi[1])
    print(pi[2])
    count = 0
    # TODO) Use a while loop to keep asking for the next digit of pi
    for d in pi:
        digit = simpledialog.askstring(title="user", prompt="What is the next digit of pi?")
        print(d)
        print(digit)
        print()
        print()
        if digit == d:
            messagebox.showinfo(title="user", message="correct")
            count += 1
        else:
            messagebox.showinfo(title="user", message="incorrect")
            messagebox.showinfo(title="user", message="You got m")
            quit(0)

# TODO) If they are correct, print "correct".
    #  If they are not, print "incorrect" and break out of the while loop

    # TODO) Print out how many digits of pi the user was able to recite in a row
