from cmath import log
import discord
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.environ['MTA3MzEwMTU4NzUwMjg3MDYxOQ.GJGjAL.plSNWFd4NookNseLcOigTpK9AqKrzZqrxHc7SA']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'call':
        await message.channel.send("callback!")

    if message.content.startswith(f'hello'):
        await message.channel.send('Hello!')


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
