#!/usr/bin/env python      
from Tkinter import *    
count = 0 
def draft(): 
    labelText.set('You drafted ' + yourPlayer.get()) 
    global count
    count += 1
    numPlayersText.set(str(count) + ' Players drafted')
    yourPlayer.delete(0, END)
    yourPlayer.insert(0, 'Next Player')
    return
players = []

app = Tk()
app.title('Fantasy Football Drafter')
app.geometry('600x400')

labelText = StringVar()
labelText.set('Click to draft')
label1 = Label(app, textvariable=labelText, height=2)
label1.pack()

numPlayersText = StringVar()
numPlayersText.set('0 Players drafted')
label2 = Label(app, textvariable=numPlayersText, height=2)
label2.pack()

drafted = StringVar(None)
yourPlayer = Entry(app, textvariable=drafted) 
yourPlayer.pack()

button1 = Button(app, text="Draft player", width=20, command=draft)
button1.pack(padx=15, pady=15)

app.mainloop()                        
