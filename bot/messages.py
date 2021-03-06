import discord, requests, json, random
from words import greetings, g_responses, sad
from discord.ext import commands

class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        username = message.author.mention
        message.content = message.content.casefold()
        message_array = message.content.split(" ")

        # Send a message if a greeting is sent
        if message_array[0] in greetings:
            await message.channel.send('Hi ' + username + ', ' + g_responses[random.randint(0, len(g_responses) - 1)] +'?')
        
        # Send a message if a sad message is sent
        if any(x in message.content for x in sad):
            inspirational_quote = get_quote()
            await message.channel.send('Cheer up ' + username + ', life gets better! Here\'s an inspirational quote for you :\) \n' + inspirational_quote)

    # Send a message when a new user joins the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Hi {member.mention}, welcome to The Skate Park!')        


# Gets a quote from zenquotes.io
def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return(quote)


# Add class to bot
def setup(bot):
    bot.add_cog(Messages(bot))
