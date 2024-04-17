

from pymongo import MongoClient
from termcolor import colored
from datetime import datetime

# connect to MongoDB cluster
# you need to add your own MonggoDB account and password
# this is more like a diary than socialmedia
cluster = MongoClient("mongodb+srv:/V/@socialmedia.ymctdku.mongodb.net/")
db = cluster["socialmedia"]["messaging"]

# Retrieve all messages from the collection
all_message = db.find({})
date = datetime.now().strftime("%x")

for message in all_message:
    try:
        if date == message["date"]:
            print(colored(f"Today - {message['time']}", 'red'))
        else:
            print(colored(f"{message['date']} - {message['time']}", 'red'))

        print(colored("From: ", 'green'), message['id'])
        print(colored("Message: ", 'green'), message['message'])
        print("---------------------------------------------------------------")
    except:
        pass


# prompt for new message
person = input("Name: ")
message = input("Message: ")

# Prepare message document (%x for date %X for time)
current_time = datetime.now().strftime("%x %X")
msg ={"id": person, "message": message, "date": date, "time": current_time}

print(msg) # Print the new message for verification

# Insert the new message into the collection
db.insert_one(msg)




