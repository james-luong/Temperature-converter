from tkinter import *
import random


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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()
