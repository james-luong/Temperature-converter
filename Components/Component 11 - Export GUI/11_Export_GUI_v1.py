from tkinter import *
from functools import partial # to prevent unwanted windows

class Convertor:
    def __init__(self):

        #Formatting variables
        background_colour = 'light blue'

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

        # Export button (row 1)
        self.export_button = Button(self.converter_frame, text='Export',
                                    font=('Arial', '14'), padx=10, pady=10,
                                    command=self.export_activate)
        self.export_button.grid(row=1)

    def export_activate(self):
        get_export = Export(self)

class Export:
    def __init__(self, partner):
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
        self.export_text.grid(row=1)

        # Filename entry box
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font='arial 14 bold', justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Save/Cancel frame
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=4, pady=10)

        # Save and Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text='Save',
                                  font='arial 12 bold')
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text='Cancel',
                                    font='arial 12 bold',
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()
