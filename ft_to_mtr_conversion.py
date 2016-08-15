#!/bin/py
# Import tkinter module, widgets
from tkinter import * 
from tkinter import ttk 

# define calculate function 
def calculate(*args): 
	try: 
		value = float(feet.get()) # Take input from entry widget, make it a float 
		meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0) # conversion 
	except ValueError: 
		pass 

# Draw main window 
root = Tk()
root.title("Feet to Meters") # Title 

mainframe = ttk.Frame(root, padding="3 3 12 12") # Frame widget 
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1) # If window is resized,  
mainframe.rowconfigure(0, weight=1)    # let frame adjust 

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) # Widget for user input 
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))	# Label for resulting number in meters 
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W) # Calculate button to perform calculation 

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W) # Create static text labels, 
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E) # then place them on screen, 
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W) # using grid coordinates 

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5) # Place widgets on frame, with padding 

feet_entry.focus() # Place the cursor here to start 
root.bind('<Return>', calculate) # Accept the return key as user input 

root.mainloop() # event loop 
