import tkinter as tk
# create a simple windows 
root=tk.Tk()
# provides title of window
root.title("simple windows app")
# set the size of window
root.geometry("480x350")
# create a label widget
label=tk.Label(root,text="Hello, My name is Paree", font=("Arial",20)) 
# set a position with some padding top to bottom
label.pack(pady=20)
# print the window 
root.mainloop()