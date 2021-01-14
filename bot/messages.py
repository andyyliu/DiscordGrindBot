import discord, requests, json, random
from words import greetings, sad

def messages(message):
    username = '@' + message.author.name
    message_array = message.content.split(" ")
    # Respond when a message thats starts with string in greetings is sent
    if message_array[0] in greetings:
        phrase = ['Hi ' + username + ' how are you?']
        return phrase

    # Respond when a message with string in sad is sent
    if any(x in message.content for x in sad):
        inspirational_quote = get_quote()
        phrase = ['Cheer up, life gets better! ' + username + ', here\'s an inspirational quote for you :\)', inspirational_quote]
        return phrase

# Gets a quote from zenquotes.io
def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' -' + json_data[0]['a']
  return(quote)