import json
from googletrans import Translator
import discord

translator = Translator()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if ('{0.author}{0.content}'.format(message) == 'GitHub#0000'):
            content = message.embeds
            content = content[0]
            content = content.description
            content = content.split(")")[1]
            print('Message from {0.author}:{0.content}'.format(message))
            messContent = content.split("-")
            translation = translator.translate(messContent[0], dest="en")
            reply = translation.text.split("-")[0]
            await message.channel.send('{0.author}{0.content}'.format(message) +
                                       ": " + reply + " - " + messContent[1])
            return

        print('Message from {0.author}:{0.content}'.format(message))
        translation = translator.translate(message.content, dest="en")
        await message.channel.send('[en]: ' + translation.text)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
# put a working token here
token = ""
client.run(token)