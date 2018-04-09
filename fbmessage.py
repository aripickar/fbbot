import fbchat
from fbchat import Client
from fbchat.models import *
import json
key_file = 'keys.json'
#Edit the keys.json file with your Username and Password
with open(key_file) as f:
    keys = json.load(f)
client = Client(keys['username'], keys['password'])
friends_file = 'friends.json'
#add all freinds that want to be messaged to friends.json with the 
#form "friendX" : "Friend name" with X as friend number
with open(friends_file) as g:
	friends = json.load(g)
print(len(friends))
#Change to support your candidate!
candidate = 'Will Wang'
for i in range(1, len(friends) + 1):
	users = client.searchForUsers(friends['friend' + str(i)])
	user = users[0]
	print("User's ID: {}".format(user.uid))
	print("User's name: {}".format(user.name))
	print("User's profile picture url: {}".format(user.photo))
	print("User's main url: {}".format(user.url))
	client.send(Message(text= 'Hi ' + str(user.name).split()[0] + '!Vote for ' + candidate + ' at sa2018.vote/' + candidate.split()[0].lower, thread_id=user.uid, thread_type=ThreadType.USER)
client.logout()
