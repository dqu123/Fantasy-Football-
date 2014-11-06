#!/usr/bin/env python      
import json
import Tkinter as tk
import os

# Import Player data from json/players.json
json_file = open('../../json/players.json')
players_json = json.load(json_file)
players = players_json['Players']
json_file.close() 

results = open('../../html/results.html', 'w')
results.write('<!DOCTYPE html> \n <html>\n <body> \n')
results.write('<h1>Draft Summary</h1>\n')
results.write('<table>\n<tr><th>Player</th><th>Position</th></tr>\n')

# A list of all the names of the players
names = []
for i in range(len(players)):
    if players[i]['active'] == '1':
        names.insert(len(names), players[i]['displayName'] + ' ' + players[i]['position'])
# Set to 100, experimenting with how many the drop down menu can handle.
names = names[:2000:20]
# Number of players drafted per team
draft_player_size = 15

count = 0 
def draft(): 
    global menuChoice, count, names, app, draft_player_size
    choice = menuChoice.get()
    labelText.set('You drafted ' + choice + '!')
    if choice[-1] !=  'K':
        results.write('<tr><td>' + choice[:len(choice)-3] + '</td>\n')
        results.write('<td>' + choice[len(choice)-3:] + '</td></tr>\n')
    else:
        results.write('<tr><td>' + choice[:len(choice)-1] + '</td>\n')
        results.write('<td>' + choice[len(choice)-1:] + '</td></tr>\n')
    names.remove(choice)
    menuChoice.set(names[0])
    option['menu'].delete(0, 'end')
    for n in names:
        option['menu'].add_command(label=n, command=tk._setit(menuChoice, n))
    count += 1
    numPlayersText.set(str(count) + ' Players drafted out of ' + str(draft_player_size))
    if count == draft_player_size:
        app.quit()
        results.write('</table> </body> \n </html>')
        results.close()
        os.system('google-chrome ../../html/results.html')
    return


app = tk.Tk()
app.title('Fantasy Football Drafter')
app.geometry('600x400')

labelText = tk.StringVar()
labelText.set('Click to draft')
label1 = tk.Label(app, textvariable=labelText, height=2)
label1.pack()

numPlayersText = tk.StringVar()
numPlayersText.set('0 Players drafted out of ' + str(draft_player_size))
label2 = tk.Label(app, textvariable=numPlayersText, height=2)
label2.pack()

menuChoice = tk.StringVar(app)
menuChoice.set(names[0])


option = tk.OptionMenu(app, menuChoice, *names)
option.pack()

# Button 
button1 = tk.Button(app, text="Draft player", width=20, command=draft)
button1.pack(padx=15, pady=15)


app.mainloop()

