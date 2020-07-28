from tkinter import *

# Top level window
window = Tk()

window.title("Studyfied.com")
window.geometry('350x200')

# Create listbox
listbox = Listbox(window, activestyle = NONE)
listbox.pack()

# Insert five items at end of the list
listbox.insert(END, "Item 1")
listbox.insert(END, "Item 2")
listbox.insert(END, "Item 3")
listbox.insert(END, "Item 4")

# Insert at index 0.
listbox.insert(0, "Item 0")

window.mainloop()
