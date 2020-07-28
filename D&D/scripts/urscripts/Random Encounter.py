from tkinter import *
import pygame
import time
import random


path = "Encounter\\"
main = "Random Encounter"
txt = ".txt"
width =30
tk = Tk()
tk.geometry("350x150")
tk.title('Random Entcounter')
tk.iconbitmap('random encounter.ico')

def role():
    u = {}
    x = str(w.get())
    fullpath = path+x+txt
    #print(fullpath)
    f = open(fullpath,"r")
    z = 0
    for y in f:
        #print(y)
        u[z] = y
        z = z+1
    #print(u)
    f.close()
    r=random.randint(0,z)
    #print(str(u[r]))
    try:
        rand.config(text=str(u[r]))
    except:
        pass








menuf = Frame(tk,relief=RIDGE, bd=2)
Label(menuf,text="Path: ").grid(row=0,column=0)
w = Entry(menuf)
w.insert(0, main)
w.grid(row=0,column=1)
Label(menuf,text=txt).grid(row=0,column=2)
menuf.pack()
f = Frame(tk,relief=RIDGE, bd=2)
rand = Label(f,text=txt)
rand.grid(row=0,column=0)
f.pack(fill=X)

role()
rol = Button(tk, text='rol',width=5,command=role).pack(side=BOTTOM)










tk.mainloop()
