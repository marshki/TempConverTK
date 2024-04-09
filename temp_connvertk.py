#!/usr/bin/env python3
# pylint: disable=too-many-ancestors
# pylint: disable=invalid-name

"""No-frills temperature conversion utility in Python2 & Python3.
"""

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

def convert_f2c(f_in):
    """Convert the value in temp_data from Fahrenheit to Celsius
    and store the result in out_data."""

    return (f_in - 32) * 5 / 9

def convert_c2f(c_in):
    """Convert the value in temp_data from Celsius to Fahrenheit
    and store the result in out-data."""

    return (c_in * 1.8) + 32

class MainWindow(tk.Frame):
    """Tkinter main window class.
    """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.config(menu=MenuBar(self))

        self.mode = 'f2c'

        self.label_in = tk.Label(self, text='Temperature in Fahrenheit:')
        self.label_in.pack()

        self.temp_in = tk.DoubleVar(value=0)
        text = tk.Entry(self, textvar=self.temp_in)
        text.pack()

        self.temp_out = tk.StringVar(self, '-17')
        lbl = tk.Label(self, textvar=self.temp_out)
        lbl.pack()

        btn = tk.Button(self, text='Convert', command=self.convert)
        btn.pack()

        btn = tk.Button(self, text='Quit', command=master.destroy)
        btn.pack()

    def f2c_mode(self):
        """Fahrenheit to Celsius mode for GUI.
        """

        self.mode = 'f2c'
        self.label_in.config(text='Temperature in Fahrenheit:')

    def c2f_mode(self):
        """Celsius to Fahrenheit mode for GUI.
        """

        self.mode = 'c2f'
        self.label_in.config(text='Temperature in Celsius:')

    def convert(self):
        """Convert user input via GUI, return conversion.
        """

        try:
            if self.mode == 'f2c':
                temp_out = convert_f2c(self.temp_in.get())
            else:
                temp_out = convert_c2f(self.temp_in.get())
            self.temp_out.set("{:.3f}".format(temp_out))
        except ValueError as e:
            self.temp_out.set("ERROR: {}".format(e))

class MenuBar(tk.Menu):
    """Menu bar class.
    """

    def __init__(self, master):
        tk.Menu.__init__(self, master)

        file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='F to C mode', command=master.f2c_mode)
        file_menu.add_command(label='C to F mode', command=master.c2f_mode)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.quit)

def main():
    """Main function.
    """

    window = tk.Tk()
    window.title("Temp Utility")
    frame = MainWindow(window)
    frame.pack()
    window.mainloop()

if __name__ == '__main__':
    main()
