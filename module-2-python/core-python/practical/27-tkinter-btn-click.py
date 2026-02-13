import tkinter as tk
# create a simple windows 
root=tk.Tk()

# create an function 

# provides title of window
root.title("simple click on button")
# set the size of window
root.geometry("480x350")
# create a label widget
label=tk.Label() 
# set a position with some padding top to bottom
label.pack(pady=20)
# print the window 
root.mainloop()