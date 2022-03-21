from tkinter import *
import random


class Convertor:
    def __init__(self):
        print("hello world")

        #Formatting variables
        background_colour = 'light blue'

        # converter Main screen GUI
        self.converter_frame = Frame(width=300, height=300, bg=background_colour)
        self.converter_frame.grid()

        # Temperature conversion heading (row 0)
        self.temp_convertor_label = Label(text='Temperature Converter', font=('Arial', '16', 'bold'),
                                          bg=background_colour, padx=10, pady=10)
        self.temp_convertor_label.grid(row=0)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()
