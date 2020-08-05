# version 0.2

import discord
import os #no idea what this is, but it works
from discord.ext import commands
from randomPick import random_line

client = commands.Bot(command_prefix = 'w ')



@client.event
async def on_ready():
    print('Logged in as', client.user.name)
    print('------')


async def on_message(self, message):
    ctx = await self.get_context(message)
    if ctx.prefix is not None:
        ctx.command = self.commands.get(ctx.invoked_with.lower())
        await self.invoke(ctx)
        

        
@client.command()
async def pring(ctx):
    await ctx.send(f'Prong! {round (client.latency * 1000)}ms ')


@client.command(help='Randomly picks from a food list')
async def food(ctx):
    await ctx.send(random_line('foodList.txt'))
 
@client.command(help='Randomly picks a snack item to eat')
async def snack(ctx):
    await ctx.send(random_line('snackList.txt'))
         
@client.command(help='Picks something from Aici\'s food list')
async def aicifood(ctx):      
    await ctx.send(random_line('aicifood.txt'))
            
#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')
    
   

client.run(os.getenv("DTOKEN"))
# no idea why "client.run('DTOKEN')" doesn't work but above line works
#client.run('DTOKEN')
#    causes an "Improper token has been passed" error

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