"""Converter trial 3
Make heading bigger and change the wrap
Completing temp convert function
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
                                            font='arial 10 italic',
                                            justify=LEFT, bg=background_colour,
                                            padx=10, pady=10)
        self.temp_instruction_label.grid(row=1)

        # temperature entry box
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font='arial 14 bold')
        self.to_convert_entry.grid(row=2)

        # conversion buttons frame (row 3), orchid3 | khaki1
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_conversion = Button(self.conversion_buttons_frame,
                                      text='Centigrade', font='arial 10 bold',
                                      bg='khaki1', padx=10, pady=10,
                                      command=lambda: self.temp_convert(-459))
        self.to_c_conversion.grid(row=0, column=0)

        self.to_f_conversion = Button(self.conversion_buttons_frame,
                                      text='Fahrenheit', font='arial 10 bold',
                                      bg='orchid1', padx=10, pady=10,
                                      command=lambda: self.temp_convert(-273))
        self.to_f_conversion.grid(row=0, column=1)


        # answer label (row 4)
        self.converted_label = Label(self.converter_frame,
                                     font='Arial 12 bold',
                                     fg='purple', bg=background_colour,
                                     pady=10, text='Conversion goes here...')
        self.converted_label.grid(row=4)

        # history/help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame,
                                       font='Arial 12 bold',
                                       text='Calculation History',
                                       width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font='Arial 12 bold',
                                  text='Export', width=5)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        history = []
        temp = 0
        self.to_convert_entry.configure(bg='white')

        error = '#ffafaf' # pale pink background for when entry box has errors

        # Retrieves amount entered in Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = 'no'

            # check amount is valid and convert to F
            if low == -273 and to_convert >= low:
                fah = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fah = self.round_it(fah)
                answer = f'{to_convert} degrees C is {fah} degrees F'

            # check amount is valid and convert to C
            elif low == -459 and to_convert >= low:
                cel = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                cel = self.round_it(cel)
                answer = f'{to_convert} degrees F is {cel} degrees C'

            else:
                # if input is invalid
                answer = 'Too cold'
                has_errors = 'yes'

            # display answer
            if has_errors == 'no':
                self.converted_label.configure(text=answer, fg='blue')
                self.to_convert_entry.configure(bg='white')
            else:
                self.converted_label.configure(text=answer, fg='red')
                self.to_convert_entry.configure(bg=error)



            # add answer to list for History

        except ValueError:
            self.converted_label.configure(text='Enter a number!', fg='red')
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)

        else:
            rounded = round(to_round, 1)

        return rounded


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
