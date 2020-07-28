from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image


root =Tk()
text = Entry(root,width=12)
text.pack()
def test():
    file = filedialog.askopenfilename(initialdir="C:\\Users\\tobias\\Desktop\\PNP\how to be a hero", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    image = ImageTk.PhotoImage(Image.open(file))
    image_label = Label(image=image).pack()
button = Button(root, text="open", command=test).pack()

def save_file():
        file = filedialog.asksaveasfile(title="Save file", defaultextension=".txt",
                                filetypes=(("Text files", "*.txt"),("all files","*.*")))
        file.write(str(text.get()))

button1 = Button(root, text="save", command=save_file).pack()


root.mainloop()
'''
def select_save_path():
    root = Tk()
    root.withdraw()
    save_path =  filedialog.asksaveasfile(mode='a')
    root.destroy()
    return (save_path)
'''
