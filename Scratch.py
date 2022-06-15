import os
import scratchattach as scratch3
import json
from urllib import request
import Discord


USERNAME_login = "" #Your scratch username

PROJECT_ID_login = "" #your Project id

login = "" #Your scratch password

session = scratch3.login(USERNAME_login, login)
SESSION_ID = session.session_id

conn = scratch3.CloudConnection(project_id=PROJECT_ID_login,
                                username=USERNAME_login,
                                session_id=SESSION_ID)

variables = scratch3.get_cloud(PROJECT_ID_login)

client = scratch3.CloudRequests(conn)



@client.request
def reset():
    reset = []
    print("full reset!")
    with open("coins.json", "w") as file:
        json.dump(reset, file)
    with open("Index.json", "w") as file:
        json.dump(reset, file)
    with open("messages.json", "w") as file:
        json.dump(reset, file)
    with open("messages_index", "w") as file:
        json.dump(reset, file)

    return "completed"


@client.request
def ping():
    print("Ping request received")
    return "pong"


@client.request
def Userinfo(argument1):
    print(f"Data requested for user {argument1}")
    user = scratch3.get_user(argument1.lower())

    projects = json.loads(
        request.urlopen("https://api.scratch.mit.edu/users/" + argument1.lower() +
                        "/projects").read().decode("utf-8"))

    c = 0
    favorites = 0
    loves = 0
    views = 0
    remixes = 0
    for i in projects:
        favorites = favorites + projects[c]['stats']['favorites']
        loves = loves + projects[c]['stats']['loves']
        views = views + projects[c]['stats']['views']
        remixes = remixes + projects[c]['stats']['remixes']

        c = c + 1

    messanges = json.loads(
        request.urlopen("https://api.scratch.mit.edu/users/" + argument1.lower() +
                        "/messages/count").read().decode("utf-8"))

    one = loves
    two = favorites
    three = remixes
    four = views
    fife = messanges["count"]

    user.update()

    with open("Index.json", "r") as file:
        getIndex = json.load(file)

    i = getIndex.index(argument1.lower())

    with open("coins.json", "r") as file:
        getCoins = json.load(file)

    Info = getCoins[i][argument1.lower()]["Coins"]

    data = [one, two, three, four, fife, Info]
    return data


@client.request
def Register(argument1):
    print(f"Data requested for user {argument1.lower()}")

    filename = 'coins.json'

    with open(filename, "r") as file:
        data = json.load(file)

    with open("Index.json", "r") as file:
        data2 = json.load(file)

    print(data)
    registered = False
    if argument1.lower() not in data2:
        registered = True
        with open("Settings.json", "r") as file:
            data_2 = json.load(file)
        data_3 = data_2[0]
        SCoins = data_3["start_coins"]
        entry = {argument1.lower(): {"Coins": SCoins}}
        data.append(entry)
        data2.append(argument1.lower())
        with open("Index.json", "w") as file:
            json.dump(data2, file)

    with open(filename, "w") as file:
        json.dump(data, file)
    with open("backup-coins.json", "w") as file:
        json.dump(data, file)

    return registered


@client.request
def addCoin(argument1, argument2):
    with open("Index.json", "r") as file:
        data = json.load(file)
    if argument1.lower() in data:
        with open("coins.json", "r") as file:
            data2 = json.load(file)

        data9 = data.index(argument1.lower())

        data3 = data2[data9]
        data4 = data3[argument1.lower()]
        data5 = data4['Coins']
        data6 = data5 + int(argument2)
        data7 = data.index(argument1.lower())
        data2.insert(data7, {argument1.lower(): {'Coins': data6}})
        data9 = data.index(argument1.lower())
        print(data9)
        data10 = data9 + 1
        print(data2)
        data2.remove(data2[data10])
        with open("coins.json", "w") as file:
            json.dump(data2, file)
        with open("backup-coins.json", "w") as file:
            json.dump(data2, file)
        return argument1.lower() + ':' + str(data6)


@client.request
def removeCoin(argument1, argument2):
    with open("Index.json", "r") as file:
        data = json.load(file)
    if argument1.lower() in data:
        with open("coins.json", "r") as file:
            data2 = json.load(file)

        data9 = data.index(argument1.lower())

        data3 = data2[data9]
        data4 = data3[argument1.lower()]
        data5 = data4['Coins']
        data6 = data5 - int(argument2)
        data7 = data.index(argument1.lower())
        data2.insert(data7, {argument1.lower(): {'Coins': data6}})
        data9 = data.index(argument1.lower())
        print(data9)
        data10 = data9 + 1
        print(data2)
        data2.remove(data2[data10])
        with open("coins.json", "w") as file:
            json.dump(data2, file)
        with open("backup-coins.json", "w") as file:
            json.dump(data2, file)
        return argument1.lower() + ':' + str(data6)


@client.request
def setCoin(argument1, argument2):
    with open("Index.json", "r") as file:
        data = json.load(file)
    if argument1.lower() in data:
        with open("coins.json", "r") as file:
            data2 = json.load(file)

        data6 = int(argument2)
        data7 = data.index(argument1.lower())
        data2.insert(data7, {argument1.lower(): {'Coins': data6}})
        index_data = data.index(argument1.lower())
        result = index_data + 1
        print(data2)
        data2.remove(data2[result])
        with open("coins.json", "w") as file:
            json.dump(data2, file)
        with open("backup-coins.json", "w") as file:
            json.dump(data2, file)
        return argument1.lower() + ':' + str(data6)


@client.request
def IsRegistered(argument1):
    result = False
    with open("Index.json", "r") as file:
        index = json.load(file)
    if argument1.lower() in index:
        result = True
    return result



@client.event
def News(argument1, argument2):
    Discord.send(argument1, argument2)
    return "true"



@client.event
def returnS():
  return



@client.event
def on_ready():
    print("Request handler is ready")



client.run()
