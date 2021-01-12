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
    print("We have logged in as {0.user}".format(client))

# Responses to commands and words
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message.content = message.content.casefold()
    phrase = messages(message)

    if not phrase:
        return
    else:
        for line in phrase:
            await message.channel.send(line)

#     Return a random number from 1-6 when !dice is sent
#     if message.content == '!dice':
#         await message.channel.send(username + " takes a deep breath, and rolls the die, the number is....." + str(random.randint(1,6)) + '!')

#     Return heads or tails when !coin is sent
#     if message.content == '!coin':
#         result = ["heads", "tails"]
#         await message.channel.send(username + "flips the coin as high as possible, it lands on....." + result[random.randint(1,2) - 1] + '!')


# # Gets a quote from zenquotes.io
# def get_quote():
#   response = requests.get("https://zenquotes.io/api/random")
#   json_data = json.loads(response.text)
#   quote = json_data[0]['q'] + " -" + json_data[0]['a']
#   return(quote)

token = 'Nzk4NjA4NDM1MjcyODc2MDQx.X_3gEA.eGBSiy5tR6nl23BoYJdDbWIvV30'
client.run(token)