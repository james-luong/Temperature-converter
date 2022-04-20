"""This is a copy of 09_History_GUI_v5 which is combined with the converter
function from 09_History_GUI_v1 (copy of which was saved as v1b to allow
adaption. The converter call - NOT the history function - has been copied
from 09_History_GUI_v1b
Need to change "if answer != 'Cannot be converted'" to "if has_error != 'yes'"
Removed the print statement and make the history button NORMAL
"""

from tkinter import *
from functools import partial  # to prevent unwanted windows


class Converter:
    def __init__(self):
        # formatting variables
        background_colour = 'light blue'

        # Initialise list to hold calculation history
        self.all_calculations = []

        # converter frame
        self.converter_frame = Frame(width=300, bg=background_colour, pady=10)
        self.converter_frame.grid()

        # temperature converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text='Temperature Converter',
                                        font='arial 19 bold',
                                        bg=background_colour, padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # user instructions (row 1)
        self.temp_instruction_label = Label(self.converter_frame,
                                            text='Type in the amount to be '
                                                 'converted and then '
                                                 'push one of the buttons...',
                                            font='arial 10 italic', wrap=290,
                                            justify=LEFT, bg=background_colour,
                                            padx=10, pady=10, )
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

        self.history_button = Button(self.hist_help_frame,
                                     font='Arial 12 bold',
                                     text='Calculation History',
                                     width=15,
                                     command=lambda: self.history_activate(
                                                        self.all_calculations))
        self.history_button.grid(row=0, column=0)

        if len(self.all_calculations) == 0:
            self.history_button.config(state=DISABLED)

        self.help_button = Button(self.hist_help_frame, font='Arial 12 bold',
                                  text='Export', width=5)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):

        error = '#ffafaf'  # pale pink background for when entry box has errors

        # Retrieves amount entered in Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = 'no'

            # check amount is valid
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9 / 5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = f'{to_convert} degrees C is {fahrenheit} degrees F'

            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5 / 9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = f'{to_convert} degrees F is {celsius} degrees C'

            else:
                # if input is invalid
                answer = 'Cannot be converted'
                has_errors = 'yes'

            # display answer
            if has_errors == 'no':
                self.converted_label.configure(text=answer, fg='blue')
                self.to_convert_entry.configure(bg='white')

            else:
                self.converted_label.configure(text=answer, fg='red')
                self.to_convert_entry.configure(bg='red')

            # Add answer to list for History
            if has_errors != 'yes':
                self.all_calculations.append(answer)
                self.history_button.config(state=NORMAL)

        except ValueError:
            self.converted_label.configure(text='Enter a number!', fg='red')
            self.to_convert_entry.configure(bg=error)

    # Rounding
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded

    def history_activate(self, calc_history):

        History(self, calc_history)


class History:
    def __init__(self, partner, calc_history):
        background = '#a9ef99' # Pale green

        # disable history button
        partner.history_button.config(state=DISABLED)

        # set up child window (i.e. history box)
        self.history_box = Toplevel()

        # if users press cross of top,
        # closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history,
                                                           partner))

        # set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # set up history heading (row 0)
        self.how_heading = Label(self.history_frame,
                                 text='Calculations History',
                                 font='arial 19 bold', bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text='Here are your most recent '
                                       'calculations. Please use the export '
                                       'button to create a text file of all '
                                       'your calculations for theis session',
                                  font='arial 10 italic', wrap=250,
                                  justify=LEFT, bg=background, fg='maroon',
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        # History output goes here (row 2)
        history_string = ''
        if len(calc_history) >= 7:
            for item in range(7):
                history_string += calc_history[len(calc_history)-item-1] + '\n'

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item)-1]+'\n'
                self.history_text.configure(text='Here is your calculation '
                                                 'history. You can use the '
                                                 'export button to save this '
                                                 'data to a text file if '
                                                 'desired')

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font='arial 12', justify=LEFT)
        self.calc_label.grid(row=2)

        # Export/Dismiss buttons frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame, bg=background)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export button
        self.export_button = Button(self.export_dismiss_frame,
                                    text='Export', font='arial 12 bold',
                                    padx=10, pady=10)
        self.export_button.grid(row=0, column=0, padx=5)

        # Dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame,
                                     text='Dismiss', font='arial 12 bold',
                                     padx=10, pady=10,
                                     command=partial(self.close_history,
                                                     partner))
        self.dismiss_button.grid(row=0, column=1, padx=5)



    def close_history(self, partner):
        # put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter()
    root.mainloop()
