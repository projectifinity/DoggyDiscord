import discord
import os #no idea what this is, but it works
from keepAlive import keep_alive

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
        if message.content == 'w food':
            from foodPick import random_line
            await message.channel.send(random_line('foodList.txt'))

client = MyClient()
keep_alive()
client.run(os.getenv("dtoken"))
# no idea why "client.run('dtoken')" doesn't work but above line works

