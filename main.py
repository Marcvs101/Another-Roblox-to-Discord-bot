# main.py

# Import libraries
import os
import discord
import discord.ext.commands
import logging

# Logger setup
logging.basicConfig(level=logging.INFO)

# Retrieve token
tokfile = open(file="./token.data", mode="r")
token = tokfile.readline().strip()
tokfile.close()

# Check if guilds folder exists
if not os.path.isdir("./guilds"):
    os.mkdir("./guilds")

# Command prefix structure


class CMD_Prefix:
    def __call__(self, bot, message):
        return "!"


# Get the bot
bot = discord.ext.commands.Bot(command_prefix=CMD_Prefix, help_command=None)

# Handle ready event
@bot.event
async def on_ready():
    print(str(bot.user)+" has connected to Discord!")

    print("Listing managed guilds:")
    for guild in bot.guilds:
        print("- "+str(guild.name)+" ("+str(guild.id)+")")
        print("\n List of roles in the guild:")
        for role in guild.roles:
            print("  - "+str(role.name)+" ("+str(role.id)+")")
        print("\n")

# Handle joining a server
@bot.event
async def on_guild_join(guild):
    print("Joined guild "+str(guild.name)+" ("+str(guild.id)+")")

# Handle player join
@bot.event
async def on_member_join(member):
    print(str(member.name)+" ("+str(member.id)+") has joined the guild '" +
          str(member.guild.name)+"' ("+str(member.guild.id)+")")

# Handle messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(str(message.author.name) + " ("+str(message.author.id)+") sent <"+str(message.content)+"> on channel '"+str(message.channel.name) +
          "' ("+str(message.channel.id)+") of guild '"+str(message.channel.guild.name)+"' ("+str(message.channel.guild.id)+")")

# Finally run the bot
bot.run(token)
