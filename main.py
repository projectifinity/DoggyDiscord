# version 0.2

import discord
import os #no idea what this is, but it works
from discord.ext import commands
from randomPick import random_line
import requests, json
from cocktaildb_grabber import drink_info



client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print('Logged in as', client.user.name)
    print('------')    

        
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms ')


@client.command(help='Randomly picks from a food list')
async def food(ctx):
    await ctx.send(random_line('foodList.txt'))
 
@client.command(help='Randomly picks a snack item to eat')
async def snack(ctx):
    await ctx.send(random_line('snackList.txt'))
         
@client.command(help='Picks something from Aici\'s food list')
async def aicifood(ctx):      
    await ctx.send(random_line('aicifood.txt'))
    
@client.command()
async def pytha(ctx):
    await ctx.send(random_line('pork.txt'))
    
@client.command()
async def mousa(ctx):
    await ctx.send(random_line('moose.txt'))
    
@client.command(help='Picks a classic cocktail from Serious Eats')
async def cocktail(ctx):
    await ctx.send(random_line('classic-cocktails.txt'))

@client.command(help='Picks a random mixed beverage that is either alcoholic or non-alcoholic')
async def drink(ctx):
    #grab data
    res = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')

    # converts response data to dict (like an array)
    info = json.loads(res.text)

    drinkName, direc, imgLink, pfull = drink_info(info)

    d=discord.Embed(
        title=drinkName,
    )
    d.set_thumbnail(url=imgLink)
    d.add_field(name="**Ingredients:**", value=pfull, inline=False)
    d.add_field(name="**Directions:**", value=direc, inline=False)
    await ctx.send(embed=d)






           
#If there is an error, it will answer with an error
#@client.event
#async def on_command_error(ctx, error):
#    await ctx.send(f'Error. Try "w help" ({error})')
    
   

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
