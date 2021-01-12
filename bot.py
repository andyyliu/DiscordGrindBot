import discord
import requests

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# token = 'Nzk4NjA4NDM1MjcyODc2MDQx.X_3gEA.eGBSiy5tR6nl23BoYJdDbWIvV30'
# client.run(token)