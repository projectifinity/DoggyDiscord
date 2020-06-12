import discord
import os #no idea what this is, but it works
from keepAlive import keep_alive

# commandPrefix = "w "

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)



    async def on_message(self, message):
    
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        #generates a "random" food item from list file
        # the "lower()" changes received argument to lowercase, so that the command will be recognized regardless of case
        if message.content.lower() == 'w food':
            from foodPick import random_line
            await message.channel.send(random_line('foodList.txt'))
            
        # temporary solution    
        #if 'dramad' in message.content.lower():
        #    from mydramalistSearch import drama_search
        #    await message.channel.send(drama_search())
  
        if message.content.lower().startswith('w d'):
            await message.channel.send('pong')


client = MyClient()
#keep_alive()
client.run(os.getenv("dtoken"))
# no idea why "client.run('dtoken')" doesn't work but above line works

# example code
# bot.command_prefix = nprefix