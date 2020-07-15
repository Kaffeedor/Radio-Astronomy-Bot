import discord
from time import sleep
import asyncio as asy
from random import randint as rain
from math import *


class MyClient(discord.Client):
    
    async def on_ready(self):
        print("I am Logged in. Beep Bob.")
        while True:
            await client.change_presence(activity=discord.Game("rab!help"), status=discord.Status.online)
            
            
###############################COMANDS##################################
    async def on_message(self, message):
        #print("Message by " + str(message.author) + " enthält " + str(message.content))
        if message.author == client.user:
            return

        if message.content.startswith("Hello"):
            await message.channel.send("Hello there!", tts=True)
            sleep(1)
            await message.channel.send("https://tenor.com/view/grevious-general-kenobi-star-wars-gif-11406339")

        elif message.content.startswith("rab!help"):
            embedd = discord.Embed(title="__**Help**__", colour=discord.Colour.blue())
            embedd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
            embedd.add_field(name="rab!help", value="To display all Commands", inline=False)
            embedd.add_field(name="Hello", value="Secret", inline=False)
            await message.channel.send(embed=embedd)
		
	elif message.content.startswith("rab!calc"):
		calculation_string = str(message.content)[8:]
		calculation_output = eval(calculation_string)
		await message.channel.send(calculation_output)

        
        else:
            pass

            
#########################################################################

            
##########################moderation#####################################
    async def on_typing(self, channel, user, when):
        pass

    async def on_message_delete(self, message):
        channel = client.get_channel(657875763546161153)
        await channel.send("**Deleted message:** `" + message.content + "` **by:** `" + str(message.author) + "`")

    async def on_message_edit(self, before, after):
        if str(after.author) != "Radio Astronomy Bot#0553":
            channel = client.get_channel(657875763546161153)
            embedd = discord.Embed(title="__**Message Edited**__", description="A Message got Edited", colour=discord.Colour.green())
            embedd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
            embedd.add_field(name="Information", value="**ID:** `"+str(before.id)+"`**; Channel:** `"+str(before.channel)+"` **; Author:** `" + str(after.author)+"`", inline=False)
            embedd.add_field(name="**Changed Message Before:**", value="`"+before.content+"`", inline=True)
            embedd.add_field(name="‏‏‎ ‏‏‎", value="-->", inline=True)
            embedd.add_field(name="**Changed Message After:**", value="`"+after.content+"`", inline=True)
            await channel.send(embed=embedd)
        else:
            pass

    async def on_member_join(self, member):
        channel = client.get_channel(657875763546161153)
        await channel.send(str(member) + " has joined!")
    
    async def on_member_remove(self, member):
        channel = client.get_channel(657875763546161153)
        await channel.send(str(member) + " has left!")
    
#    async def on_member_update(self, before, after):
 #       channel = client.get_channel(657875763546161153)
  #      await channel.send("`" + "a user..." + "` **changed nickname from** `" + str(before.nick) + "` **to** `" + str(after.nick) + "`")
        
    
#########################################################################   
                                


        
          
client = MyClient()
client.run("NzI5MjQzMzA2NzY4MzM0ODY4.XwGG8A.Am8Uw_TuyJ35YByyaGwl6J8frKI")
