# version 0.2

import discord
import os #no idea what this is, but it works
from discord.ext import commands
from randomPick import random_line
import requests, json
from cocktaildb_grabber import drink_info
from mydramalistSearch import drama_link



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
async def drink(ctx, *args):

    #checks if tuple, args, is empty
    if (len(args) == False):

        # calls for random drink
        drinkName, direc, imgLink, pfull = drink_info(info)
    
    # tuple has arguments    
    else:
        ingredientFilter = ' '.join(args)
        drinkID = drink_filter_returns_rdm_id(ingredientFilter)
        info = drink_by_id(drinkID) 

        print (info)

        drinkName, direc, imgLink, pfull = drink_info(info)

        print (drinkName, direc, imgLink, pfull)


    d=discord.Embed(
        title=drinkName,
    )
    d.set_thumbnail(url=imgLink)
    d.add_field(name="**Ingredients:**", value=pfull, inline=False)
    d.add_field(name="**Directions:**", value=direc, inline=False)
    await ctx.send(embed=d)


@client.command(help='Searches MyDramaList')
async def drama(ctx, *args):
    search = ' '.join(args)
    print ('Search terms: ' + search)

    res = requests.get("https://kuryana.vercel.app/search/q/" + search)
    dramaData = json.loads(res.text)
   
    await ctx.send(drama_link(dramaData))



           
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
