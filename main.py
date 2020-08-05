# version 0.2
# trying to align code with recommended form in documentation
# capitalizing variables (ongoing) as it seems to be a python convention?

import discord
import os #no idea what this is, but it works
from discord.ext import commands
from randomPick import random_line

# CMD_PREFIX = "w "
client = commands.Bot(command_prefix = 'w ')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
        
@client.command(name='pring')
async def pring(ctx):
    await ctx.send(f'Prong! {round (client.latency * 1000)}ms ')


@client.command()
async def food(ctx):
    await ctx.send(random_line('foodList.txt'))
    #generates a "random" food item from list file

 
@client.command()
async def snack(ctx):
    await ctx.send(random_line('snackList.txt'))
         
@client.command()
async def aicifood(ctx):      
    ctx.send(random_line('aicifood.txt'))
            
#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')
    
   

client.run(os.getenv("DTOKEN"))
# no idea why "client.run('DTOKEN')" doesn't work but above line works
#client.run('DTOKEN')

# temporary solution    
#if 'dramad' in message.content.lower():
#    from mydramalistSearch import drama_search
#    await message.channel.send(drama_search())

  
#        # this thing doesn't work, no idea why
#        if message.content.startswith('pring'):
#            await message.channel.send('pong')
#            print ("oknn")

# example code
# bot.command_prefix = nprefix
# ctx means context