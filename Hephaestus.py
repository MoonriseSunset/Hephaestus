# Dev: MoonriseSunset
# License: MIT

#To use this framework, take a look at the README or at the github page :)
#Bot permission integer: 137439472704
#NOTE: this program will NOT run correctly by itself! There are parts of the code that need to be filled in by the user.

#All the initial imports and variables we need
import discord
from secret import BotID
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#The trigger and prefix variables store what will trigger the bot if seen in a message
#Either can be disabled by disabling the respective trigger/prefixEnabled variable to False
#Note that the trigger and prefix are case-INSENSITIVE, check the README on how to make it case-sensitive.
trigger = ""
triggerEnabled = False

prefix = "!"
prefixEnabled = True

#The Raw and -input list variables store the user's message as well as modified forms of it
Raw = []        #stores any raw message detected by the bot, even if the message doesn't trigger it
Input = []      #stores the message split up into individual letters without the prefix
Cinput = []     #Concatenated-Input
Winput = []     #Word-Input, stores the triggered input but is split into the individual words.
command = ""    #the command variable stores the 0th index value of Winput, which will have whatever command the user makes

#integer which tells the cutter function at what index value the actual message - the prefix/command starts
startAt = 0

#These next lines print a confirmation that the python file has successfully logged into the bot.
@client.event
async def on_ready():
    print(f'Success! The program has logged into {client.user}')

#Here is the main part of the code, which is triggered whenever a message is sent in a channel the bot can access
@client.event
async def on_message(message):

    #this function can be triggered by the bot itself, so this statement stops the bot from responding to itself
    if message.author == client.user:
        return

    Raw = [message.content,]    #storing the user message

    if(
        str(str(Raw[0])).lower().find(trigger,0,(len(trigger))) == 0 and triggerEnabled == True or
        message.content.startswith(prefix) and prefixEnabled == True
    ):  #This massive statement is what lets the bot tell if it should act or not
        
        #This next block removes the prefix/trigger from the message and stores it in our Input lists.
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

        #an example of how to create a command
        if(command == "hi"):
            await message.channel.send("Hello there!")




        Input.clear()
        Cinput.clear()
        Winput.clear()
        Raw.clear()         #Clearing all the lists so that the bot doesn't get bogged down with previous messages
        
client.run(BotID)