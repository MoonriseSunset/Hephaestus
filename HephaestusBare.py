# Dev: MoonriseSunset
# License: MIT

#To use this framework, take a look at the README or at the github page :)
#Bot permission integer: 137439472704
#NOTE: this program will NOT run correctly by itself! There are parts of the code that need to be filled in by the user.

import discord
from secret import BotID
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#Note that the trigger and prefix are case-INSENSITIVE, check the README on how to make it case-sensitive.
trigger = ""
triggerEnabled = False

prefix = "!"
prefixEnabled = True

Raw = []        
Input = []      
Cinput = []     
Winput = []     
command = ""    

startAt = 0

@client.event
async def on_ready():
    print(f'Success! The program has logged into {client.user}')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    Raw = [message.content,]

    if(
        str(str(Raw[0])).lower().find(trigger,0,(len(trigger))) == 0 and triggerEnabled == True or message.content.startswith(prefix) and prefixEnabled == True):
        
        if(message.content.startswith(prefix) == True):
            startAt = len(prefix) - 1
        else:
            startAt = len(trigger)
        for count, letter in enumerate(Raw[0]):
            if(count > startAt):
                Input.append(letter)
        Cinput = [''.join(Input),]
        Winput = Cinput[0].split()
        command = str(Winput[0]).lower()

        if(command == "hi"):
            await message.channel.send("Hello there!")




        Input.clear()
        Cinput.clear()
        Winput.clear()
    Raw.clear()   
        
client.run(BotID)