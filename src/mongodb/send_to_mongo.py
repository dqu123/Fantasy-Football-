import json
import pymongo
# Move JSON data into p
f = open('../json/players.json')
p = json.load(f)
f.close()
p = p['Players']

# set up JSON client
client = pymongo.MongoClient()
db = client.fantasy_football
players = db.players  
player_id = players.insert(p)
