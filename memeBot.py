import discord
from discord.ext import commands 
import random

memeList = open("memeList.txt")
memeCollection = open("memeCollection.txt")
 
client = commands.Bot(command_prefix = '.') #the prefix (,!;)

@client.event
async def on_ready():
    print("Bot is ready.")

client.run('ODA2MTYxOTYyOTMyMTA5MzYz.YBla1Q.MLRhA8MXxSdRsOcv2KC8poudWP8')

def get_meme():
    memeCount = 0

    for line in memeList:
        memeCount += 1

    randomMeme = random.randint(1, memeCount)

    memeFind = 1

    for line in memeList:
        if memeFind == randomMeme:
            return line
        memeFind += 1

def meme_collection():
    pass
    #TODO

def num_of_memes():
    memeCount = 0

    for line in memeCollection:
        memeCount += 1

    return memeCount

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return

    if message.content.startswith("hello"):
        await message.channel.send("hello, I am a bot.")

        if message.author == "beeboo#1940":
            await message.channel.send("HIHI" + message.author + ":3")

    if message.content.startswith("I love you"):
        await message.channel.send("I love you too!")
      
    if message.content.startswith("!myCollection"):
        await message.channel.send(my_collection())


client.run('ODA2MTYxOTYyOTMyMTA5MzYz.YBla1Q.FOE5i13mnjuFGYkdXg0VPImYG2o')

    

        
            
