import discord
from generate import gentext

client = discord.Client()

token = open('token.txt').read()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('s!ping'):
        await message.channel.send('peng :^)')

    if message.content.startswith('s!spit'):
        await message.channel.send(gentext())

    if message.content.startswith('s!help'):
        await message.channel.send("use s!spit to generate text, thats literally it lmao. oh and s!github for github link :sunglasses:")

    if message.content.startswith('s!github'):
        await message.channel.send("https://github.com/99kaits/textbound")

client.run(token)