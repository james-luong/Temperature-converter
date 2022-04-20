"""Changed the command on history button to lambda
Then changed the history function
Add calc_history parameter to History class
Enter history output
Add label
"""

from tkinter import *
from functools import partial  # to prevent unwanted windows


class Convertor:
    def __init__(self):
        # Formatting variables
        background_colour = 'light blue'

        # Initialise list to hold calculation history
        # In later version list will be populated with user calculations
        self.all_calculations = ['0 degrees F is -17.8 degrees C',
                                 '0 degrees C is 32 degrees F',
                                 '40 degrees C is 104 degrees F',
                                 '40 degrees F is 4.4 degrees C',
                                 '12 degrees C is 53.6 degrees F',
                                 '24 degrees C is 75.2 degrees F',
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
    something = Convertor()
    root.mainloop()
