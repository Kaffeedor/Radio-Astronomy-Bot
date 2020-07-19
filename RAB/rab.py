import discord
from time import sleep
import asyncio as asy
from random import randint as rain
from math import *
import datetime
#from os import system
#from ast import literal_eval


class MyClient(discord.Client):
    
    async def on_ready(self):
        print("I am Logged in. Beep Bob.")
        while True:
            await client.change_presence(activity=discord.Game("rab!help"), status=discord.Status.online)
            
            
###############################COMANDS##################################
    async def on_message(self, message):
        #print("Message by " + str(message.author) + " enthält " + str(message.content))
        if message.author == client.user and message.author.bot == False:
            return
        
        if message.content.startswith("test"):
            await message.channel.send("nonono, this only works when kaffeedor tests something you little piece of")
            #await message.channel.send(str(message.author.roles))
            print(message.author.roles)

        elif message.content.startswith("rab!help"):
            embedd = discord.Embed(title="__**Help**__", colour=discord.Colour.blue())
            embedd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
            embedd.add_field(name="rab!help", value="To display all Commands", inline=False)
            embedd.add_field(name="rab!calc", value="Calculate something.", inline=False)
            embedd.add_field(name="rab!ban [user_id] [reason]", value="Bans a user. Only for Staff.", inline=False)
            embedd.add_field(name="rab!kick [user_id] [reason]", value="Kicks a user. Only for Staff.", inline=False)
            await message.channel.send(embed=embedd)

        
        elif message.content.startswith("rab!ban"):
            banuserid = message.content.split(" ")[1]
            try:
                banreason = message.content.split(" ")[2]
            except:
                banreason = "reason not specifified"
                
            if "Staff" in message.author.roles:
                if message.author.id != banuserid:
                    await banuserid.ban(banreason)
                    await message.channel.send(banuserid + " got banned for" + banreason + " by " + str(message.author))  
                else:
                     await message.channel.send("You cant ban yourself bruh")
            else:
                 await message.channel.send("You cant use that command")

        elif message.content.startswith("rab!kick"):
            kickuserid = message.content.split(" ")[1]
            try:
                kickreason = message.content.split(" ")[2]
            except:
                kickreason = "reason not specifified"
                
            if "Staff" in message.author.roles:
                if message.author.id != kickuserid:
                    await kickuserid.kick(kickreason)
                    await message.channel.send("`" + kickuserid + "` got banned for `" + kickreason + "` by " + str(message.author))  
                else:
                     await message.channel.send("You cant kick yourself bruh")
            else:
                 await message.channel.send("You cant use that command!")

            
        elif message.content.startswith("rab!calc"):
            calculation_string = str(message.content)[8:]
            calculation_output = eval(calculation_string)

            if len(str(calculation_output)) <= 2000:
                await message.channel.send(calculation_output)
            else:
                await message.channel.send("'Too Big' or something")

        
        else:
            pass

            
#########################################################################

            
##########################moderation/logging#####################################
    async def on_typing(self, channel, user, when):
        pass

    async def on_message_delete(self, message):
            channel = client.get_channel(657875763546161153)
            embedd = discord.Embed(title="__**Message Deleted**__", description="A Message got Deleted", colour=discord.Colour.red())
            embedd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
            embedd.add_field(name="Information", value="**ID:** `"+str(message.id)+"`**; Channel:** `"+str(message.channel)+"` **; Author:** `" + str(message.author)+"`", inline=False)
            embedd.add_field(name="**Deleted Message:**", value="`"+message.content+"`", inline=False)
            await channel.send(embed=embedd)

    async def on_message_edit(self, before, after):
        if str(after.author) != "Radio Astronomy Bot#0553" and message.author.bot == False:
            channel = client.get_channel(657875763546161153)
            embedd = discord.Embed(title="__**Message Edited**__", description="A Message got Edited", colour=0xe4b400)
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
        channel1 =client.get_channel(657877136878862336)
        rai=client.get_channel(657877179417493534)
        v=client.get_channel(660829108250345472)
        r=client.get_channel(660914279729332224)
        embedd = discord.Embed(title="__**Member Joined**__", description="A Member joined the server.", colour=discord.Colour.green())
        embedd.set_thumbnail(url=member.avatar_url)
        embedd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
        embedd.add_field(name="Member", value="@" + str(member), inline=False)
        embedd.add_field(name="Member ID:", value=str(member.id), inline=False)
        a = member.created_at
        b = datetime.datetime.now()
        dhms=b-a
        embedd.add_field(name="**Account Creation:**", value=str(dhms) + " days, hours, minutes, seconds ago", inline=False)
        await channel.send(embed=embedd)
        await channel1.send("Hey " + member.mention + ", welcome to **Radio Astronomy and Space**:tada::hugging:! Please read the Rules in " + rai.mention + ", verify yourself in " + v.mention + " and give yourself roles in " + r.mention)
    
    async def on_member_remove(self, member):
        channel = client.get_channel(657875763546161153)
        channel1 = client.get_channel(657877136878862336)
        embedd = discord.Embed(title="__**Member Left**__", description="A Member left the server.", colour=discord.Colour.red())
        embedd.set_thumbnail(url=member.avatar_url)
        embedd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
        embedd.add_field(name="Member", value="@" + str(member), inline=False)
        embedd.add_field(name="Member ID:", value=str(member.id), inline=False)
        await channel.send(embed=embedd)
        await channel1.send("**" + str(member) + "** just left the server:slight_frown:")
    
#    async def on_member_update(self, before, after):
 #       channel = client.get_channel(657875763546161153)
  #      await channel.send("`" + "a user..." + "` **changed nickname from** `" + str(before.nick) + "` **to** `" + str(after.nick) + "`")
        
    
#########################################################################   
                                



        
          
client = MyClient()
client.run("TOKEN")
