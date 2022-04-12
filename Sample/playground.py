# from tkinter import *
# from tkinter import ttk
# from ttkthemes import ThemedTk
# from random import *
#
#
# root = Tk()
# canvas = Canvas(root, width=400, height=300, bg='white')
#
#
# def draw(event=None):
#     canvas.delete(ALL)  # clear canvas first
#     canvas.create_oval(randint(0, 399), randint(0, 299), 15, 15, fill='red')
#
#
# draw()
# canvas.pack()
#
# root.bind("<space>", draw)
# root.mainloop()

# string = "If opportunity doesn't knock, build a door.\n" \
# "optimism is an occupational hazard of programming: feedback is the treatment.\n" \
# "if opportunity doesn;t knock, build a door.\nCode is like humor. When you have to explain it, its bad."
#
#
# list = ['If', 'opportunity', "doesn't", 'knock,', 'build', 'a', 'door.\noptimism', 'is', 'an', 'occupational', 'hazard',
#         'of', 'programming:', 'feedback', 'is', 'the', 'treatment.\nif', 'opportunity', 'doesn;t', 'knock,', 'build',
#         'a', 'door.\nCode', 'is', 'like', 'humor.', 'When', 'you', 'have', 'to', 'explain', 'it,', 'its', 'bad.\n\n']
#
# formatted = string.split("\n")
# print(formatted)

# string = " Code is like humor. When you have to explain it, its bad. In order to be irreplaceable, one must always be different When to use iterative development? You should use iterative development only on projects that you want to succeed."
# print(string.strip(" "))

import sys
import os

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

if __name__ == "__main__":
    answer = input("Do you want to restart this program ? ")
    if answer.lower().strip() in "y yes".split():
        restart_program()
