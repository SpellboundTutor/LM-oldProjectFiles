import tkinter as tk #You can shorten the name as "as". Alias for the module.

def putmsg(from_widget, to_widget): #sets one variable from one entry box to the other entry box, back and forth, while erasing the prior entry box.
    to_widget.set(from_widget.get)
    from_widget.set("")

def main():
    root = tk.Tk() #Create a root, to a constructor in Tk. Stored in variable "root"
    root.geometry("800x600") #Width and height of window.
    root.title("Zac's Example of TK") #Will display title at top of screen; doesn't show on Chrome for some reason.

    frm = tk.Frame(root, padx=10, pady=10) #Frame; empty box. Adds it to the root. Feel free to Google these things. So many attributes to customize!
    #pass through "root" or anything that contains a function into this. Padding adds empty space between things in the frame.
    frm.grid() #Layout manager; Treats the frame as a grid, with rows and columns. 

    tk.Label(frm, text="1").grid(column=0, row=0) #Label: A bit of text that goes on layout manager. the Frame "owns" this function. Giving the text as 1, sending it to the grid to assign its location.

    entry_var = tk.StringVar() #Text entry bar
    entry = tk.Entry(frm, text="", textvariable=entry_var) #stores text in variable
    entry.grid(column=1, row=0)

    tk.Label(frm, text="2").grid(column=0, row=1)

    btn1 = tk.Button(frm, text="1 -> 2", command=lambda: purmsg(entry_var, entryvar2)) #command can equal any function, but the function cannot take any arguments! If you use a function that requires information, you can use lambda, which passes putmsg and its variables through the function.
    root.mainloop #Must use this to kick off the main loop for Tk
