# Dev: MoonriseSunset
# License: MIT

# To use this framework, take a look at the README or at the github page :)
# Bot permission integer: 137439472704
# NOTE: this program will NOT run correctly by itself! There are parts of the code that need to be filled in by the user.

import discord
from discord.ext import commands
from secret import BotID

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Note that the trigger and prefix are case-INSENSITIVE, check the README on how to make it case-sensitive.
trigger = ""
triggerEnabled = False

prefix = "!"
prefixEnabled = True

# Create bot instance with command prefix
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'Success! The program has logged into {bot.user}')
    print(f'Bot ID: {bot.user.id}')
    print(f'Discord.py version: {discord.__version__}')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Store original message content
    raw_content = message.content
    
    # Check if message starts with trigger or prefix
    should_process = False
    start_at = 0
    
    if triggerEnabled and trigger and raw_content.lower().startswith(trigger.lower()):
        should_process = True
        start_at = len(trigger)
    elif prefixEnabled and raw_content.startswith(prefix):
        should_process = True
        start_at = len(prefix)
    
    if should_process:
        # Extract the command and arguments
        command_input = raw_content[start_at:].strip()
        word_input = command_input.split()
        
        if word_input:  # Make sure there's at least one word
            command = word_input[0].lower()
            
            # Command handling
            if command == "hi":
                await message.channel.send("Hello there!")
            elif command == "ping":
                await message.channel.send("Pong!")
            elif command == "info":
                embed = discord.Embed(
                    title="Bot Information",
                    description=f"Running Discord.py {discord.__version__}",
                    color=0x00ff00
                )
                await message.channel.send(embed=embed)
    
    # Process commands (important for commands.Bot)
    await bot.process_commands(message)

# Example slash command (modern Discord feature)
@bot.slash_command(name="hello", description="Say hello!")
async def hello_slash(ctx):
    await ctx.respond("Hello from slash command!")

# Example traditional command using commands framework
@bot.command(name="test")
async def test_command(ctx, *, args=None):
    """A test command"""
    if args:
        await ctx.send(f"You said: {args}")
    else:
        await ctx.send("This is a test command!")

# Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Ignore command not found errors
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument!")
    else:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    try:
        bot.run(BotID)
    except discord.LoginFailure:
        print("Invalid bot token!")
    except Exception as e:
        print(f"An error occurred while running the bot: {e}")
