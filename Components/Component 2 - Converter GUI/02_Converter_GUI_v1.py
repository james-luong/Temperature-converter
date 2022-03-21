"""Converter GUI v1
Basic tkinter template copied from 00_tkinter_template.py
and based on the planning done in Trello (component 2 - slide 17)
"""


from tkinter import *
from functools import partial # to prevent unwanted additional windows
import random


class Converter:
    def __init__(self):
        # formatting variables
        background_colour = 'light blue'

        # converter frame
        self.converter_frame = Frame(width=300, bg=background_colour, pady=10)
        self.converter_frame.grid()

        # temperature converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text='Temperature Converter',
                                        font='arial 16 bold',
                                        bg=background_colour, padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # user instructions (row 1)
        self.temp_instruction_label = Label(self.converter_frame,
                                            text='Type in the amount to be '
                                                 'converted and then '
                                                 'push one of the buttons...',
                                            font='arial 10 italic', wrap=250,
                                            justify=LEFT, bg=background_colour,
                                            padx=10, pady=10)
        self.temp_instruction_label.grid(row=1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
