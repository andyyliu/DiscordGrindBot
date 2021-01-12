import discord
import requests
import json
import random
from messages import messages
from commands import commands

client = discord.Client()

# Initial login
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Responses to commands and words
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    message.content = message.content.casefold()
    # Respond to messages
    phrase = messages(message)
    if phrase:
        for line in phrase:
            await message.channel.send(line)
    
    #Respond to commands
    phrase = commands(message)
    if phrase:
        for line in phrase:
            await message.channel.send(line)

token = 'Nzk4NjA4NDM1MjcyODc2MDQx.X_3gEA.eGBSiy5tR6nl23BoYJdDbWIvV30'
client.run(token)