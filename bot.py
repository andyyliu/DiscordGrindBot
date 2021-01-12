import discord
import requests
import json
from words import *

client = discord.Client()

# Initial login
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Gets a quote from zenquotes.io
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

# Responses to commands and words
@client.event
async def on_message(message):
    message.content = message.content.casefold()
    if message.author == client.user:
        return

    # Respond when a message thats starts with string in greetings is sent
    if message.content.startswith(tuple(greetings)):
        await message.channel.send('Hi @' + message.author.name + ' how are you?')
    
    # Respond when a message wit hstring in sad is sent
    if any(x in message.content for x in sad):
        inspirational_quote = get_quote()
        await message.channel.send("You will be ok @" + message.author.name + ", here's an inspirational quote for you :\)")
        await message.channel.send(inspirational_quote)
    

token = 'Nzk4NjA4NDM1MjcyODc2MDQx.X_3gEA.eGBSiy5tR6nl23BoYJdDbWIvV30'
client.run(token)