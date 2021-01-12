import discord, requests, json, random
from words import *

def commands(message):
    username = '@' + message.author.name

    # Return a random number from 1-6 when !dice is sent
    if message.content == '!dice':
        phrase = [username + " takes a deep breath, and rolls the die, the number is....." + str(random.randint(1,6)) + '!']
        return phrase

    # Return heads or tails when !coin is sent
    if message.content == '!coin':
        result = ["heads", "tails"]
        phrase = [username + "flips the coin as high as possible, it lands on....." + result[random.randint(1,2) - 1] + '!']
        return phrase