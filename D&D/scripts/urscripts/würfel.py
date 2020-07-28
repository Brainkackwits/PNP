from tkinter import *
import pygame
import time
import random


width =25
tk = Tk()
tk.geometry("350x150")
tk.title('Würfel')
tk.iconbitmap('Dice.ico')
f = Frame(tk,relief=RIDGE, bd=2)
#global würfel
def role():
    try:
        wuerfelwert = int(würfel.get())
        i=random.randint(1,wuerfelwert)
        laberol = Label(f, text=i,width=5)
        laberol.grid(row=0,column=1)

        ge = int(eingabe1.get())
        ver = int(eingabe0.get())

        eingabe1.delete(0, END)
        eingabe0.delete(0, END)
        labever = Label(f, text=ver,width=5)
        labever.grid(row=0,column=0)
        labege = Label(f, text=ge,width=5)
        labege.grid(row=0,column=2)
        eingabe1.insert(0, '20')
        eingabe0.insert(0, '10')
        if ge > i and i > ver:
            #NORMAL
            laberol.config(bg = '#ffb3fe')
            text.config(text = 'Win')
        if ver == i or ver > i:
            #VERLOREN
            labever.config(bg = 'red2')
            text.config(text = 'Lose')
        if ge == i or i > ge :
            #GEWONNEN
            labege.config(bg = 'SpringGreen2')
            text.config(text = 'Super Win')
        if i == wuerfelwert:
            laberol.config(bg = 'SpringGreen2')
        if i == 1:
            laberol.config(bg = 'red2')
            text.config(text = 'Super Lose')
    except:
        pass
    #pass

menuf = Frame(tk)

label = Label(menuf, text='Würfel',width=5).grid(row=0,column=0)


würfel = Entry(menuf,width=5)
würfel.grid(row=0,column=1)
würfel.insert(0, '20')



norwürfel = Label(menuf, width=width,text=' 4 | 6 | 8 | 10 | 12 | 20 ').grid(row=0,column=2)

exit = Button(menuf, text='back',width=5,command=tk.destroy).grid(row=0,column=3)
menuf.pack()




gamemenuf = Frame(tk,relief=RIDGE, bd=2)

label = Label(gamemenuf, text='Verloren ab:',width=width).grid(row=1,column=0)
eingabe0 = Entry(gamemenuf,width=width)
eingabe0.grid(row=2,column=0)
eingabe0.insert(0, '10')
label = Label(gamemenuf, text='Gewonnen ab:',width=width).grid(row=1,column=1)
eingabe1 = Entry(gamemenuf,width=width)
eingabe1.grid(row=2,column=1)
eingabe1.insert(0, '20')
gamemenuf.pack()
f.pack()


rol = Button(tk, text='rol',width=5,command=role).pack(side=BOTTOM)

labelf = Frame(tk,relief=RIDGE, bd=2)
text = Label(labelf,width=width)
text.grid(row=0,column=0)
labelf.pack(side=BOTTOM)








tk.mainloop()
