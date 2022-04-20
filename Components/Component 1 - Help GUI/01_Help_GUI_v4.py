from tkinter import *
import random
from functools import partial # to prevent unwanted windows

class Convertor:
    def __init__(self):
        print("hello world")

        #Formatting variables
        background_colour = 'light blue'

        # converter Main screen GUI
        self.converter_frame = Frame(width=300, height=300, bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Temperature conversion heading (row 0)
        self.temp_convertor_label = Label(self.converter_frame, text='Temperature Converter',
                                          font=('Arial', '16', 'bold'), bg=background_colour, padx=10, pady=10)
        self.temp_convertor_label.grid(row=0)

        # Export button (row 1)
        self.help_button = Button(self.converter_frame, text='Export', font=('Arial', '14'),
                                  padx=10, pady=10, command=self.help_activate)
        self.help_button.grid(row=1)

    def help_activate(self):
        print('You asked for help')
        get_help = Help(self)
        get_help.help_text.configure(text='Enter a number in the box and then push one of the buttons'
                                          'to convert to either degrees Celsius (deg C) or degrees Fahrenheit (deg F)')


class Help:
    def __init__(self, partner):
        background = 'orange'

        # disable help button
        partner.help_button.config(state=DISABLED)

        # set up child window (i.e. help box)
        self.help_box = Toplevel()

        # set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set up help heading (row 1)
        self.how_heading = Label(self.help_frame, text='Export/Instructions', font='arial 10 bold', bg=background)
        self.how_heading.grid(row=0)

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text='', justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text='Dismiss', width=10, bg='orange',
                                  font='arial 10 bold', command=self.close_help)
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self):
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()
