import tkinter
from tkinter import *
import datetime
import time
#main window everything goes in
MainWindow = Tk()
#Sections of the window
topframe = Frame(MainWindow, bg="#323232")
topframe.pack(side=TOP)
bottomframe = Frame(MainWindow, bg="#323232")
bottomframe.pack(side=BOTTOM)
rightframe = Frame(MainWindow, bg="#323232")
rightframe.pack(side=RIGHT)
leftframe = Frame(MainWindow, bg="#323232")
leftframe.pack(side=LEFT)
today = datetime.date.today()
ddday = datetime.date(1111, 11, 11)
dday = today - ddday
#functions
def refresh_equation():
    global dday
    dday = today - ddday
    print ("Displaying Days")
    label.config(text = dday.days)
def ww1s():
    global ddday
    print ("Calculating Days")
    ddday = datetime.date(1914, 7, 28)#WW1 start date
    refresh_equation()
def ww1e():
    global ddday
    print ("Calculating Days")
    ddday = datetime.date(1918, 11, 11)#WW1 end date
    refresh_equation()
def ww2s():
    global ddday
    print ("Calculating Days")
    ddday = datetime.date(1939, 9, 1)#WW2 start date
    refresh_equation()
def ww2e():
    global ddday
    print ("Calculating Days")
    ddday = datetime.date(1945, 9, 2)#WW2 end date
    refresh_equation()
def koreas():
    global ddday
    print ("Calculating Days")
    ddday = datetime.date(1950, 6, 25)#Korean War start date
    refresh_equation()
def koreae():
    global ddday
    print ("Calculating Days")
    ddday = datetime.date(1953, 7, 27)#Korean War end date
    refresh_equation()
def vietnams():
    global ddday
    print ("Calculating Days")
    ddday = datetime.date(1955, 11, 1)#Vietnam War start date
    refresh_equation()
def vietname():
    global ddday
    print ("Calculating Days")
    ddday = datetime.date(1975, 4, 30)#Vietnam War end date
    refresh_equation()
def reset():
    print ("reset")
    label.config(text ="")
def dayinput():
    print ("user input")
    global today
    e1 = int(entry1.get())
    e2 = int(entry2.get())
    e3 = int(entry3.get())
    usi = datetime.date(e1, e2, e3)
    useri = today - usi
    useroutput.config(text=useri.days)
def reset2():
    print ("reset user input")
    useroutput.config(text="")
#items on screen
TITLE = Label(leftframe, text="Important wars of the 20th Century", bg="#323232", fg="white", font="none 15")
label = Label(leftframe, text="", font="none 20", bg="#323232", fg="white")
ww1sb = Button(leftframe, text="WW1 Start", command=ww1s, bg="orange")
ww1eb = Button(leftframe, text="WW1 End", command=ww1e, bg="green")
ww2sb = Button(leftframe, text="WW2 Start", command=ww2s, bg="orange")
ww2eb = Button(leftframe, text="WW2 End", command=ww2e, bg="green")
koreasb = Button(leftframe, text="Korean War Start", command=koreas, bg="orange")
koreaeb = Button(leftframe, text="Korean War End", command=koreae, bg="green")
vietnamsb = Button(leftframe, text="Vietnam War Start", command=vietnams, bg="orange")
vietnameb = Button(leftframe, text="Vietnam War End", command=vietname, bg="green")
resetb = Button(leftframe, text="Reset", command=reset, bg="red")
TITLE2 =Label(rightframe, text="Input your own date", bg="#323232", fg="white", font="none 15")
entry1 = Entry(rightframe)
entry2 = Entry(rightframe)
entry3 = Entry(rightframe)
syntax =Label(rightframe, text="YYYY, MM, DD", bg="#323232", fg="white", font="none 15")
go = Button(rightframe, text="Go", bg="green", command=dayinput)
reset2 = Button(rightframe, text="Reset", command=reset2, bg="red")
useroutput = Label(rightframe, text="", bg="#323232", fg="white", font="none 15") 
#making those items
TITLE.pack()
label.pack()
ww1sb.pack()
ww1eb.pack()
ww2sb.pack()
ww2eb.pack()
koreasb.pack()
koreaeb.pack()
vietnamsb.pack()
vietnameb.pack()
resetb.pack()
TITLE2.pack()
syntax.pack()
entry1.pack()
entry2.pack()
entry3.pack()
go.pack(side=LEFT)
reset2.pack(side=LEFT)
useroutput.pack()
#window stuff
MainWindow.title("Day Counter")
MainWindow.geometry("700x331")
MainWindow.configure(background="#323232")
MainWindow.resizable(0,0)
MainWindow.mainloop()
