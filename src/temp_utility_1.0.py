#!/bin/py
# Python 3.4.3 
import tkinter
from tkinter import ttk 

def convert(out_data, temp_data):
    """ Convert the value in temp_data, assumed to be in degrees Fahrenheit,
        to Celsius and store the result in out_data. """ 
    try: 
    	f = temp_data.get()
    	out_data.set((f - 32) * 5 / 9)
    except ValueError:
        pass

window = tkinter.Tk()
window.title("Temp Tool")
frame = tkinter.Frame(window)
frame.pack()

out_data = tkinter.StringVar()
temp_data = tkinter.DoubleVar()

tkinter.Label(frame, text='Temperature in Fahrenheit:').pack()

text = tkinter.Entry(frame, textvar=temp_data)
text.pack()

label = tkinter.Label(frame, textvar=out_data)
label.pack()

button = tkinter.Button(frame, text='Convert', command=lambda: convert(out_data, temp_data))
button.pack()

button2 = tkinter.Button(frame, text='Quit', command=lambda: window.destroy())
button2.pack()

window.mainloop()
