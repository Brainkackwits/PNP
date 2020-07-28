from tkinter import *
import pygame
import time
import random
import os

width =25
path = "NPC-generator\\"

global armorwert
global ruestunguse
global hpwert
global fullname
global classlist
global u
global dexteritystat
global armorw
global rüstungw
global initw
global hpw
txt = ".txt"
def save1():
    try:
        from tkinter import filedialog
        file = filedialog.asksaveasfile(initialdir="NPC-generator\\NPC's",title="Save file",
                                            defaultextension=".NPC",
                                            filetypes=(("NPC file", "*.NPC"),("all files","*.*")))
        savelist = {}
        file.write(str(fullname))
        file.write(str(fullold))
        file.write("\n"+str(rasse))
        file.write(str(classlist))


        file.write(str(waffe1))
        file.write(str(items1))


        file.write(str(strength))
        file.write("\n"+str(dexterity))
        file.write("\n"+str(constitution))
        file.write("\n"+str(intelligence))
        file.write("\n"+str(wisdom))
        file.write("\n"+str(charisma))

        file.write("\n"+str(taverne))

        file.write(str(armorwert))
        file.write("\n"+str(hpwert))
        file.close()
    except:
        pass
def paste():
    #try:
            global u
            u = {}
            main = "rassen"
            fullpath = path+main+txt
            #print(fullpath)
            f = open(fullpath,"r")
            z = 0
            for y in f:
                #print(y)
                u[z] = y
                z = z+1
            f.close()
            global strength
            global dexterity
            global constitution
            global intelligence
            global wisdom
            global charisma
            global waffe1
            global items1
            name1.config(text=fullname)
            classe1.config(text=classlist)
            rasse1.config(text=rasse)
            old1.config(text=fullold)
            tavernew.config(text=taverne)
            try:
                waffenw1.config(text=waffe1)
                itemw.config(text=items1)
            except:
                pass
            strengthw.config(text=strength)
            dexterityw.config(text=dexterity)
            constitutionw.config(text=constitution)
            intelligencew.config(text=intelligence)
            wisdomw.config(text=wisdom)
            charismaw.config(text=charisma)
            q=["0","0","0","0","0","0"]
            z=0
            s = 0
            d = 0
            co = 0
            i= 0
            w=0
            ch=0
            #print(u)
            #print(rasse)
            if rasse == "Drachengeborene"or rasse == u[0]:
                s=2
                ch=2
            if rasse == "Elfen"or rasse == u[1]:
                d=2
                w=2
            if rasse == "Halblinge"or rasse == u[2]:
                d=2
                ch=2
            if rasse == "Orks"or rasse == u[3]:
                s=2
                co=2
            if rasse == "Halbelfen"or rasse == u[4]:
                ch=2
                co=2
            if rasse == "Zwerge"or rasse == u[6]:
                d=2
                co=2
            if rasse == "Drow"or rasse == u[7]:
                d=2
                ch=2
            if rasse == "Gnome"or rasse == u[8]:
                i=2
                ch=2
            if rasse == "Goblins"or rasse == u[9]:
                d=2
                ch=2
            if rasse == "Kobold"or rasse == u[10]:
                d=2
                co=2
            #print(strength,dexterity,constitution,intelligence,wisdom,charisma)
            for g in [int(strength),int(dexterity),int(constitution),int(intelligence),int(wisdom),int(charisma)]:

                if g == 18:
                    gc=4
                if g <= 17:
                    gc=3
                if g <= 15:
                    gc=2
                if g <= 13:
                    gc=1
                if g <= 11:
                    gc=0
                if g <= 9:
                    gc = -1
                if g <= 7:
                    gc = -2
                if g <= 5:
                    gc = -3
                if g <= 3:
                    gc = -4
                #clear()
                q[z] = gc
                z = z+1


            #print(q)
            z = 0
            for g in q:
                u = Label(statsf, width=9,text=str(g))
                u.grid(row=2,column=z+1)
                if z == 1:
                    global dexteritystat
                    dexteritystat = g
                    #print(dexteritystat)
                z = z+1
            gc = q[0]+s
            q[0] = gc
            gc = q[1]+d
            q[1] = gc
            gc = q[2]+co
            q[2] = gc
            gc = q[3]+i
            q[3] = gc
            gc = q[4]+w
            q[4] = gc
            gc = q[5]+ch
            q[5] = gc
            z=0
            for g in q:
                u = Label(statsf, width=9,text=str(g))
                u.grid(row=3,column=z+1)
                #print(str(z)+" "+str(g))

                z = z+1






            try:
                global rüstungw
                global initw
                global hpw
                global armorwert
                global ruestunguse
                global hpwert
                global armorw
                armorw.config(text=armorwert)
                rüstungw.config(text=ruestunguse)
                initw.config(text=dexteritystat)
                hpw.config(text=hpwert)
            except:
                pass



def open1():
    try:
        from tkinter import filedialog
        file = filedialog.askopenfilename(initialdir="NPC-generator\\NPC's",
                                        title="Select A File",
                                        filetypes=(("NPC file", "*.NPC"),
                                        ("all files","*.*")))
        #open
        try:
            file = open(file)
            i = 0
            y = {}
            for x in file:
                y[i] = x
                #print(x)
                i = i+1
            global fullname
            global fullold
            global rasse
            global classlist
            global waffe1
            global items1
            global strength
            global dexterity
            global constitution
            global intelligence
            global wisdom
            global charisma
            global taverne
            global armorwert
            global hpwert

            fullname = str(y[0] + y[1])
            fullold = str(y[2])
            rasse= str(y[3])
            classlist= str(y[4])
            waffe1= str(y[5] + y[6])
            items1= str(y[7]+y[8] + y[9])
            strength= str(y[10])
            dexterity= str(y[11])
            constitution= str(y[12])
            intelligence= str(y[13])
            wisdom= str(y[14])
            charisma= str(y[15])
            taverne= str(y[16]+y[17])

            armorwert= str(y[18])
            hpwert= str(y[19])
            #print(fullname)





        except:
            pass
        paste()
    except:

        pass
    pass

def role():
    global classlist
    global armorwert
    global ruestunguse
    global hpwert
    def names():

        #name
        a = {}
        main = "male"
        fullpath = path+main+txt
        #print(fullpath)
        f = open(fullpath,"r")
        z = 0
        for y in f:
            #print(y)
            a[z] = y
            z = z+1
        #print(u)
        f.close()

        u = {}
        main = "female"
        fullpath = path+main+txt
        #print(fullpath)
        f = open(fullpath,"r")
        z = 0
        for y in f:
            #print(y)
            u[z] = y
            z = z+1

        f.close()
        b = {}
        main = "backname"
        fullpath = path+main+txt
        #print(fullpath)
        f = open(fullpath,"r")
        z = 0
        for y in f:
            #print(y)
            b[z] = y
            z = z+1
        #print(u)
        f.close()
        global fullname
        fullname = str(random.choice([random.choice(u),random.choice(a)]))+" "+random.choice(b)
    def rassenandclass():
        global u
        u = {}
        main = "rassen"
        fullpath = path+main+txt
        #print(fullpath)
        f = open(fullpath,"r")
        z = 0
        for y in f:
            #print(y)
            u[z] = y
            z = z+1
        global rasse
        rasse = str(random.choice(u))
        try:
            if len(str(entryrasse.get())) > 2:
                rasse = str(entryrasse.get())
        except:
            pass

        main = "class"
        global classlist
        classlist = {}
        fullpath = path+main+txt
        #print(fullpath)
        f = open(fullpath,"r")
        classno = 0
        for y in f:
            #print(y)
            classlist[classno] = y
            classno = classno+1
        #print(classlist)
        f.close()
        classlist = random.choice(classlist)
        try:
            if len(str(entryclass.get())) > 2:
                classlist = str(entryclass.get())
        except:
            pass
    def old():
        global fullold
        fullold = str(random.choice(["alt","jung","mittel"]))
    def rolstats():
        global strength
        global dexterity
        global constitution
        global intelligence
        global wisdom
        global charisma


        strength = random.randint(1, 6) + random.randint(1, 6)+ random.randint(1, 6)
        dexterity = random.randint(1, 6) + random.randint(1, 6)+ random.randint(1, 6)
        constitution = random.randint(1, 6) + random.randint(1, 6)+ random.randint(1, 6)
        intelligence = random.randint(1, 6) + random.randint(1, 6)+ random.randint(1, 6)
        wisdom = random.randint(1, 6) + random.randint(1, 6)+ random.randint(1, 6)
        charisma = random.randint(1, 6) + random.randint(1, 6)+ random.randint(1, 6)
    def roltaverne():
        Taverne = {}
        main = "Taverne"
        fullpath = path+main+txt
        #print(fullpath)
        f = open(fullpath,"r")
        z = 0
        for y in f:
            #print(y)
            Taverne[z] = y
            z = z+1

        #print(a)
        f.close()
        Taverne1 = {}
        main = "Tavernex"
        fullpath = path+main+txt
        #print(fullpath)
        f = open(fullpath,"r")
        z = 0
        for y in f:
            #print(y)
            Taverne1[z] = y
            z = z+1

        #print(a)
        f.close()
        global taverne
        taverne = random.choice(Taverne)
        Taverne1 = random.choice(Taverne1)

        taverne = str(taverne)+" "+str(Taverne1)
    def rolinventar():
        a = {}
        main = "items\\waffen"
        fullpath = path+main+txt
        #print(fullpath)
        f = open(fullpath,"r")
        z = 0
        for y in f:
            #print(y)
            a[z] = y
            z = z+1

        #print(a)
        f.close()
        waffenno = random.randint(1,3)

        c = random.randint(0,int(len(a)))
        d = random.randint(0,int(len(a)))

        while a[c]== a[d]:
            if a[d] == "Deager" or a[d] == "Sword":
                break
            c = random.randint(0,int(len(a)))
            d = random.randint(0,int(len(a)))

        d=a[d]
        c=a[c]
        global waffe1
        waffe1 = ""+str(d)+" "+str(c)




        a = {}
        main = "items\\items"
        fullpath = path+main+txt
        #print(fullpath)
        f = open(fullpath,"r")
        z = 0
        for y in f:
            #print(y)
            a[z] = y
            z = z+1

        #print(a)
        f.close()
        waffenno = random.randint(1,3)

        c = random.randint(0,int(len(a)))
        d = random.randint(0,int(len(a)))
        b = random.randint(0,int(len(a)))
        while a[c]== a[d] and a[c]== a[b]:

            c = random.randint(0,int(len(a)))
            d = random.randint(0,int(len(a)))
            b = random.randint(0,int(len(a)))

        d=a[d]
        c=a[c]
        b=a[b]
        global items1
        items1 = str(d)+" "+str(c)+" "+str(b)
    def ruestunghp():
        ALVL = str(Alvl.get())
        if ALVL != str(1) or ALVL != str(2) or ALVL != str(3):
            rüstunglist = [0]
        if ALVL == str(1):
            rüstunglist = [11,11,12]
        if ALVL == str(2):
            rüstunglist = [12,13,14,14,15]
        if ALVL == str(3):
            rüstunglist = [14,16,17,18]
        global armorwert
        global ruestunguse
        global hpwert
        ruestunguse = random.choice(rüstunglist)
        #print(ruestunguse)

        armorwert = random.randint(10,16)
        armorwert = armorwert+ruestunguse
        #print(armorwert)
        hpwert = round((random.randint(10,16)+random.randint(10,16)+random.randint(10,16))/3)


    names()
    rassenandclass()
    old()
    rolstats()
    roltaverne()
    ruestunghp()

    try:
        rolinventar()
    except:
        pass
#while False:

    paste()


def edit():
    edit=Toplevel(tk)
    edit.geometry("550x70+120+50")
    edit.resizable(width=0, height=0)
    edit.title('NPC edit')
    edit.iconbitmap('Goblin.ico')
    roll = Button(edit, text='rol',width=5,command=role)
    roll.grid(row=0,column=0)
    #
    global entryrasse
    global entryclass
    entry1rasse = Label(edit,text="Rasse").grid(row=1,column=0)
    entryrasse = Entry(edit,width=25)
    entryrasse.grid(row=3,column=0)
    #
    entry1class = Label(edit,text="Class").grid(row=1,column=1)
    entryclass = Entry(edit,width=25)
    entryclass.grid(row=3,column=1)

    pass
global armorw
def combat():
    #role()
    combat = Toplevel(tk)
    combat.geometry("1100x200+670+120")
    combat.resizable(width=0, height=0)
    combat.title('NPC Combat')
    combat.iconbitmap('Goblin.ico')
    roll = Button(combat, text='rol',width=5,command=role)
    roll.grid(row=0,column=0)

    combatf = Frame(combat)
    box = Label(combat,width=10)
    box.grid(row=0,column=1)
    talent = Label(combat,text="Talente",width=10)
    talent.grid(row=4,column=0)

    Acrobatics = Label(combat,text="Acrobatics").grid(row=5,column=0)
    Animalhandling  = Label(combat,text="Animalhandling").grid(row=5,column=1)
    Arcana = Label(combat,text="Arcana").grid(row=5,column=2)
    Athletics = Label(combat,text="Athletics").grid(row=5,column=3)
    Deception = Label(combat,text="Deception").grid(row=5,column=4)
    History = Label(combat,text="History").grid(row=5,column=5)
    Insight = Label(combat,text="Insight").grid(row=5,column=6)
    Intimidation = Label(combat,text="Intimidation").grid(row=5,column=7)
    Investigation = Label(combat,text="Investigation").grid(row=5,column=8)
    Medicine = Label(combat,text="Medicine").grid(row=5,column=9)
    Nature = Label(combat,text="Nature").grid(row=5,column=10)
    Perception = Label(combat,text="Perception").grid(row=5,column=11)
    Performance = Label(combat,text="Performance").grid(row=5,column=12)
    Persuasion = Label(combat,text="Persuasion").grid(row=5,column=13)
    Religion = Label(combat,text="Religion").grid(row=5,column=14)
    SleightofHand = Label(combat,text="Sleight of Hand").grid(row=5,column=15)
    Stealth = Label(combat,text="Stealth").grid(row=5,column=16)
    Survival = Label(combat,text="Survival").grid(row=5,column=17)
    '''
        Acrobaticsw = Label(combat)
        Animalhandlingw = Label(combat)
        Arcanaw = Label(combat)
        Athleticsw = Label(combat)
        Deceptionw = Label(combat)
        Historyw = Label(combat)
        Insightw = Label(combat)
        Intimidationw = Label(combat)
        Investigationw = Label(combat)
        Medicinew = Label(combat)
        Naturew = Label(combat)
        Perceptionw = Label(combat)
        Performancew = Label(combat)
        Persuasionw = Label(combat)
        Religionw = Label(combat)
        SleightofHandw = Label(combat)
        Stealthw = Label(combat)
        Survivalw = Label(combat)'''






    global initw
    init = Label(combat,text="Initiative")
    init.grid(row=0,column=1)
    initw = Label(combat)
    initw.config(text=str(dexteritystat))
    initw.grid(row=1,column=1)

    global rüstungw

    armor = Label(combat,text="Armor")
    armor.grid(row=0,column=2)
    global armorw
    armorw = Label(combat)
    armorw.config(text=str(armorwert))
    armorw.grid(row=1,column=2)
    rüstung = Label(combat,text="Rüstung")
    rüstung.grid(row=2,column=2)
    rüstungw = Label(combat)
    rüstungw.config(text=str(ruestunguse))
    rüstungw.grid(row=3,column=2)
    global hpw
    hp = Label(combat,text="HP",width=8)
    hp.grid(row=0,column=3)
    hpw = Label(combat,width=8)
    hpw.config(text=str(hpwert))
    hpw.grid(row=1,column=3)

    pass



tk = Tk()
tk.geometry("550x300+120+120")
tk.resizable(width=0, height=0)
tk.title('NPC Generator')
tk.iconbitmap('Goblin.ico')


mainf = Frame(tk)
f = Frame(mainf,relief=RIDGE, bd=2)
name = Label(f,text="NAME :")
name.grid(row=0,column=0)
name1 = Label(f,width=15,height=3)
name1.grid(row=1,column=0)

old = Label(f,text="OLD :")
old.grid(row=0,column=1)
old1 = Label(f,width=15,height=2)
old1.grid(row=1,column=1)

rasse = Label(f,text="Rasse :")
rasse.grid(row=0,column=2)
rasse1 = Label(f,width=15,height=2)
rasse1.grid(row=1,column=2)
classe = Label(f,text="Class :")
classe.grid(row=2,column=2)
classe1 = Label(f,width=15,height=2)
classe1.grid(row=3,column=2)

inv = Label(f,text="Inventar :")#muss noch
inv.grid(row=0,column=3)
waffenw1 = Label(f,height=3)
waffenw1.grid(row=1,column=3)

itemw = Label(f,width=15,height=4)
itemw.grid(row=3,column=3)

#inv1 = Label(f,width=15)
#inv1.grid(row=1,column=3)
#inv2 = Label(f,width=15)
#inv2.grid(row=2,column=3)
#inv3 = Label(f,width=15)
#inv3.grid(row=3,column=3)

f.pack(fill=X,side=TOP)

statsf = Frame(mainf,relief=RIDGE, bd=2)

save = Label(statsf, width=12,text="Saving Throws")
save.grid(row=3,column=0)
strengthw = Label(statsf, width=9)
strengthw.grid(row=1,column=1)

stats = Label(statsf, width=12,text="Stats")
stats.grid(row=2,column=0)
strengthw1 = Label(statsf, width=9)
strengthw1.grid(row=2,column=1)
strength = Label(statsf, width=9,text='STRENGTH')
strength.grid(row=0,column=1)

dexterityw = Label(statsf, width=9)
dexterityw.grid(row=1,column=2)
dexterity = Label(statsf, width=9,text='DEXTERITY')
dexterity.grid(row=0,column=2)

constitutionw = Label(statsf, width=9)
constitutionw.grid(row=1,column=3)
constitution = Label(statsf, width=12,text='CONSTITUTION')
constitution.grid(row=0,column=3)

intelligencew = Label(statsf, width=9)
intelligencew.grid(row=1,column=4)
intelligence = Label(statsf, width=11,text='INTELLIGENCE')
intelligence.grid(row=0,column=4)


wisdomw = Label(statsf, width=9)
wisdomw.grid(row=1,column=5)
wisdom = Label(statsf, width=7,text='WISDOM')
wisdom.grid(row=0,column=5)



charismaw = Label(statsf, width=9)
charismaw.grid(row=1,column=6)
charisma = Label(statsf, width=9,text='CHARISMA')
charisma.grid(row=0,column=6)

#role()
werte = Button(statsf, width=12,text="Combat",command=combat)
werte.grid(row=0,column=0)
statsf.pack(fill=X)
mainf.pack(side=BOTTOM)

menuf = Frame(tk,relief=RIDGE, bd=2)

mainmenu = Menubutton(menuf, text="Menu")
mainmenu.grid(row=0,column=1)
#Filemenu
submenu = Menu(mainmenu)
mainmenu.config(menu=submenu)

submenu.add_command(label="Edit",command=edit)
submenu.add_command(label="Open",command=open1)
submenu.add_command(label="Save",command=save1)
submenu.add_command(label="Rol",command=role)







L = Label(menuf,text="Armor LVL :",height=2).grid(row=0,column=4)
Alvl = Entry(menuf,width=2)
Alvl.grid(row=0,column=5)
blank = Label(menuf,text="",width=width,height=2).grid(row=0,column=9)
taverne = Label(menuf,text="Taverne: ").grid(row=0,column=10)

tavernew = Label(menuf,height=2)
tavernew.grid(row=0,column=11)
menuf.pack(side=TOP,fill=X)
role()



rol = Button(menuf, text='rol',width=5,command=role)
rol.grid(row=0,column=6)




tk.mainloop()
