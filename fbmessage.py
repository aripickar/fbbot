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
candidate = 'William Wang'
for i in range(1, len(friends) + 1):
	users = client.searchForUsers(friends['friend' + str(i)])
	user = users[0]
	print("User's ID: {}".format(user.uid))
	print("User's name: {}".format(user.name))
	print("User's profile picture url: {}".format(user.photo))
	print("User's main url: {}".format(user.url))
	messages = ('Hi ' + str(user.name).split()[0] + '! It is asuc elections time, and this year, I am encouraging people to vote for ' + candidate + ' at asuc.org/elections. You can read more about his platforms at studentaction.org! ',
			'Hey ' + str(user.name).split()[0] + '! Its that time of year again, and I need you to vote for  ' + candidate + ' at asuc.org/elections!. It\'s really imoportant to me, and I would love if you could help!',
			'What\'s up ' + str(user.name).split()[0] + '! It\'s voting season right now, and I need your help to get ' + candidate + ' elected. You can vote at asuc.org/elections. Thanks!',
			'Hey ' + str(user.name).split()[0] + '! ASUC elections is really important to me, and I have been working to get ' + candidate + ' elected. You can help me out at asuc.org/elections. Thanks!',
			'Hey ' + str(user.name) + '! ASUC elections are in full swing, and I\'m on the campaign of' + candidate + ', who is running for Senate. Would you mind taking 5 seconds and voting for them at asuc.org/elections? Thanks!')
	client.send(Message(text= messages[random.randint(0,4)]), thread_id=user.uid, thread_type=ThreadType.USER)
client.logout()
