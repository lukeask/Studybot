import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '.')
channelid =  ID

@client.event
async def on_ready():
    print('Ready')

#initializes study session and sets the host
@client.command(pass_context=True)
async def start(ctx, pcnumber):
    # start a study session
    global pingperson
    global number
    channel = client.get_channel(channelid)
    pingperson = ctx.author
    number = pcnumber
    await channel.send(f'Starting a session in PC{number} under {pingperson.mention}')

#change the current host
@client.command(pass_context=True)
async def changeping(ctx, member : discord.Member):
    global pingperson
    global number
    pingperson = member
    await channel.send(f'The person {pingperson.mention} will now be pinged')

#returns current chat number and pings current host
@client.command(pass_context=True)
async def letmein(ctx):
    global pingperson
    global number
    channel = client.get_channel(channelid)
    if number != 0:
        await channel.send(f'Let me into PC{number}, {pingperson.mention}')
    else:
        await channel.send('There is no active PC')

#display helptext
@client.command(pass_context=True)
async def studybothelp(ctx):
    channel = client.get_channel(channelid)
    await channel.send('Commands:')
    await channel.send('.help - brings up help text')
    await channel.send('.start n - starts a new study chat where n is the PC number')
    await channel.send('.letmein - pings the current host')
    await channel.send('.changeping @user - passes the host to @user')
    await channel.send('.endsession - ends the current session')

@client.command(pass_context=True)
async def endsession(ctx):
    global pingperson
    global number
    channel = client.get_channel(channelid)
    await channel.send('Ending the current study session')
    number = 0

client.run(TOKEN)
