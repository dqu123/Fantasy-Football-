#!/usr/bin/env python      
import json
from Tkinter import *   
import Tkinter as tk

# Import Player data from json/players.json
json_file = open('../../json/players.json')
players_json = json.load(json_file)
players = players_json['Players']

# A list of all the names of the players
names = []
for i in range(len(players)):
    if players[i]['active'] == '1':
        names.insert(len(names), players[i]['fname'] + ' ' + players[i]['lname'])
# Set to 100, experimenting with how many the drop down menu can handle.
names = names[0:100]


count = 0 
def draft(): 
    global menuChoice
    labelText.set('You drafted ' + menuChoice.get()) 
    global count, names 
    names.remove(menuChoice.get())
    menuChoice.set(names[0])
    option['menu'].delete(0, 'end')
    for n in names:
        option['menu'].add_command(label=n, command=tk._setit(menuChoice, n))
    count += 1
    numPlayersText.set(str(count) + ' Players drafted')
    return

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

menuChoice = StringVar(app)
menuChoice.set(names[0])


option = OptionMenu(app, menuChoice, *names)
option.pack()

# Button 
button1 = Button(app, text="Draft player", width=20, command=draft)
button1.pack(padx=15, pady=15)


app.mainloop()                        
