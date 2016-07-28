#!/bin/py
# Python 2 or 3 

try:
    import tkinter as tk #it's common to import tkinter as "tk"
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
 
def convert_f2c(f_in):
    """ Convert the value in temp_data from Fahrenheit to Celsius and store the result in out_data. """
    return ((f_in - 32) * 5 / 9)
 
class MainWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.config(menu=MenuBar(self))
 
        lbl = tk.Label(self, text='Temperature in Fahrenheit:')
        lbl.pack()
 
        self.f_in = tk.DoubleVar() #variables that we will use later are instance variables (start with "self.")
        text = tk.Entry(self, textvar=self.f_in) #variables that we will not use later are normal variables
        text.pack()
 
        self.c_out = tk.StringVar()
        lbl = tk.Label(self, textvar=self.c_out)
        lbl.pack()
 
        btn = tk.Button(self, text='Convert', command=self.convert)
        btn.pack()
 
        btn = tk.Button(self, text='Quit', command=master.destroy) #'master' is the same object as 'window' in the main() function
        btn.pack()
 
    def convert(self):
        try:
            temp_f = self.f_in.get()
            temp_c = convert_f2c(temp_f)
            self.c_out.set("{:.3f}".format(temp_c))
        except ValueError as e:
            self.c_out.set("ERROR: {}".format(e))
 
class MenuBar(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master)
 
        file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label='File', menu=file_menu)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.quit)
 
        self.window_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label='Windows', menu=self.window_menu)
 
        help_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='View Readme')
 
def main():
    window = tk.Tk()
    window.title("Temp Tool")
    frame = MainWindow(window)
    frame.pack()
    window.mainloop()
 
if __name__ == '__main__':
    main()
