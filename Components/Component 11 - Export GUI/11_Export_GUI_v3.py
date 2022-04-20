"""
Started with 09_History_GUI_v5
"""

from tkinter import *
from functools import partial  # to prevent unwanted windows
import re


class Converter:
    def __init__(self):
        # Formatting variables
        background_colour = 'light blue'

        # Initialise list to hold calculation history
        # In later version list will be populated with user calculations
        self.all_calculations = ['0 degrees F is -17.8 degrees C',
                                 '0 degrees C is 32 degrees F',
                                 '100 degrees F is 37.8 degrees C']

        # converter Main screen GUI
        self.converter_frame = Frame(width=300, height=300,
                                     bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Temperature conversion heading (row 0)
        self.temp_convertor_label = Label(self.converter_frame,
                                          text='Temperature Converter',
                                          font=('Arial', '16', 'bold'),
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.temp_convertor_label.grid(row=0)

        # history button (row 1)
        self.history_button = Button(self.converter_frame, text='History',
                                  font=('Arial', '14'), padx=10, pady=10,
                                  command=lambda: self.history_activate(
                                      self.all_calculations))
        self.history_button.grid(row=1)

        if len(self.all_calculations) == 0:
            self.history_button.config(state=DISABLED)

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
                                    command=lambda: self.export(calc_history),
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

    def export(self, calc_history):

        Export(self, calc_history)

class Export:
    def __init__(self, partner, calc_history):
        background = '#a9ef99'

        # disable export button
        partner.export_button.config(state=DISABLED)

        # set up child window (i.e. help box)
        self.export_box = Toplevel()

        # if users press cross of top, closes help and 'releases' help button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,
                                                             partner))

        # set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # set up export heading (row 1)
        self.how_heading = Label(self.export_frame, text='Export/Instructions',
                                 font='arial 16 bold', bg=background)
        self.how_heading.grid(row=0)

        # export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text='Enter a filename in the bos below and '
                                    'press the Save button to save your '
                                    'calculation history to a text file',
                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame,
                                 text='If the filename you enter below '
                                      'already exists, its contents will be '
                                      'replaced with you calculations history',
                                 justify=LEFT, bg='#ffafaf', fg='maroon',
                                 font='arial 10 italic', wrap=225,
                                 padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename entry box
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font='arial 14 bold', justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error message (row 4)
        self.save_error_label = Label(self.export_frame, text='', fg='maroon',
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save/Cancel frame
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text='Save',
                                  font='arial 12 bold',
                                  command=partial(lambda: self.save_history(
                                      partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text='Cancel',
                                    font='arial 12 bold',
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):
        # RegEx to check file name, can be upper or lower case letters
        valid_char = '[A-Za-z0-9_]'  # numbers or underscores
        has_error = 'no'

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue  # if the letter is valid, gets back and checks the next

            elif letter == ' ':  # otherwise, find problem
                problem = 'No spaces allowed!'

            else:
                problem = f'No {letter} is allowed!'

            has_error = 'yes'

        if filename == '':
            problem = 'Filename cannot be blank'
            has_error = 'yes'

        if has_error == 'yes':  # describe problem
            # Display error message
            self.save_error_label.config(text=f'Invalid filename - {problem}')
            # Change entry box background to pink
            self.filename_entry.config(bg='#ffafaf')
            print()

        else:
            # If there are no errors, generate text file and then close
            # dialogue
            # add /txt suffix
            filename = filename + '.txt'

            # Create file to hold data
            f = open(filename, 'w+')

            # add new line at the end of each item
            for item in calc_history:
                f.write(item + '\n')

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter()
    root.mainloop()
