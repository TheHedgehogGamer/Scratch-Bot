import os
import discord
import json
import datetime
import Scratch

TOKEN = ""  # your bot token

set_channel_id = 0  # the channel id you want to use

set_guild_id = 0  # the guild id you want to use (the bot must be on this guild)

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    channel_id = int(message.channel.id)
    guild_id = int(message.guild.id)
    if channel_id == set_channel_id:
        if guild_id == set_guild_id:
            messages_time = str(datetime.datetime.now())
            print(messages_time)
            user = str(message.author).split('#')[0].lower()
            message_content = message.content
            with open("messages.json", "r") as file:
                messages = json.load(file)
            with open("messages_index.json", "r") as file:
                messages_index = json.load(file)

            messages_index.append(user)

            messages.append(
                {user: {
                    "Message": message_content,
                    "Time": messages_time
                }})

            with open("messages.json", "w") as file:
                json.dump(list(messages), file)
            with open("messages_index.json", "w") as file:
                json.dump(list(messages_index), file)


@client.event
async def send(argument1, argument2):
    channel = client.get_channel(set_channel_id)
    await channel.message.send(argument1 + ": " + argument2)
    Scratch.returnS()
    return True


@client.event
async def on_ready():
    print('Bot logged in as {0.user}'.format(client))


client.run(TOKEN)
