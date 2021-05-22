# version 0.2

import discord
import random
import os #no idea what this is, but it works
from discord.ext import commands
from randomPick import random_line
import requests, json
from cocktaildb_grabber import drink_info, ingredient_filtered_data_returns_rdm_id, drink_by_id
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

        #grab data
        res = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')

        # converts response data to dict (like an array)
        info = json.loads(res.text)

        # gets information on random drink
        drinkName, direc, imgLink, pfull = drink_info(info)
    
    # tuple has arguments    
    else:
        ingredientFilter = ' '.join(args)

        #grab data
        res = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=' + ingredientFilter)

        # converts response data to dict (like an array)
        info = json.loads(res.text)

        drinkID = ingredient_filtered_data_returns_rdm_id(info)
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


# some commands for fun
# rps = rock paper scissors
rpsTools = ['rock', 'paper', 'scissors']  # list of rps tools

# rps rules
# value beats key
rpsRules = {'rock':'paper',
            'paper':'scissors',
            'scissors':'rock'}


@client.command(aliases = ['rps'])
async def _rps(ctx, tool = "none"):
    emoji = {'rock': ':bricks:',
             'paper': ':newspaper:',
             'scissors': ':scissors:'}
    if tool in rpsTools:
        botTool = random.choice(rpsTools)

        await ctx.send(f' {ctx.message.author.display_name} {emoji[tool]} :vs: {emoji[botTool]} bot ')

        if botTool == rpsRules[tool]:
            await ctx.send('**I win!**')
        elif botTool == tool:
            await ctx.send('Its a tie...')
        else:
            await ctx.send('You win.')
    else:
        await ctx.send(f'This is not a tool in "rock paper scissors". \n You can only use: \n {rpsTools[0]} {emoji[rpsTools[0]]} \n {rpsTools[1]} {emoji[rpsTools[1]]} \n {rpsTools[2]} {emoji[rpsTools[2]]}')



           
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
