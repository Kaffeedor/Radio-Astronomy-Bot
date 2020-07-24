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
        channel = client.get_channel(731756741058101248)
        embedd = discord.Embed(title="I am Logged in. Beep Bob.", description="Bob Beep", colour=discord.Colour.green())
        embedd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
        await channel.send(embed=embedd)

        channel = client.get_channel(660914279729332224)
        embeddd = discord.Embed(title="__**Roles**__", description="Here you can give yourself Roles with reacting to Emojies", colour=discord.Colour.dark_green())
        embeddd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
        embeddd.add_field(name="Radio Astronomy Roles:", value="-:red_circle: for _Experienced Radio Amateur_ \n -:orange_circle: for _Radio Astronomy Amateur_ \n -:yellow_circle: for _Radio Astronomy Beginner_", inline=False)
        embeddd.add_field(name="Astronomy Roles:", value="-:green_circle: for _Astronomer_ \n -:blue_circle: for _Stargazer_", inline=False)
        #await channel.send(embed=embeddd)
        embedddd = discord.Embed(title="__**Region Roles**__", colour=discord.Colour.purple())
        embedddd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
        embedddd.add_field(name="Northern Hemisphere:", value="-:heart: for _North America_ \n -:orange_heart: for _Europe_ \n -:yellow_heart: for _Asia_", inline=False)
        embedddd.add_field(name="Southern Hemisphere:", value="-:green_heart: for _South America_ \n -:blue_heart: for _Africa_ \n -:purple_heart: for _Australia and Oceania_ \n -:white_heart: for _Antartica_", inline=False)
        #await channel.send(embed=embedddd)
        embeddddd = discord.Embed(title="__**Other Roles**__", colour=discord.Colour.red())
        embeddddd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
        embeddddd.add_field(name="Notify Roles:", value="-:coffee: for _Kaffe's YT Notify", inline=False)
        embeddddd.add_field(name="Feed Roles:", value="-:rocket: for _Space News_", inline=False)
        #await channel.send(embed=embeddddd)
        embedddddd = discord.Embed(title=" ", colour=0xFFFFFF)
        embedddddd.add_field(name="Requestable Roles:", value="-_Professional Radio Astronomer_ \n -_Content Creator_ \n -_Trusted_ is for active and trustworthy Members, estimated by Staff.", inline=False)
        embedddddd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
        #await channel.send(embed=embedddddd)
        while True:
            await client.change_presence(activity=discord.Game("rab!help"), status=discord.Status.online)

##### COMMANDS #####
    async def on_message(self, message):
        #print("Message by " + str(message.author) + " enthält " + str(message.content))
        if message.author == client.user and message.author.bot == False:
            return

# Verify Bot Status
        if message.content.startswith("test"):
            await message.channel.send("kek")
            #await message.channel.send(str(message.author.roles))660914279729332224
            print(message.channel.id)

# List Available Commands
        elif message.content.startswith("rab!help"):
            embedd = discord.Embed(title="__**Help**__", colour=discord.Colour.blue())
            embedd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
            embedd.add_field(name="rab!help", value="Displays all Available Commands.", inline=False)
            embedd.add_field(name="rab!calc ", value="Calculate Something. (Make a Space between Calculation and `calc`.)", inline=False)
            embedd.add_field(name="rab!antennacalc [antenna type] [Paramters]", value="Calculates a Antenna.\n -__Antenna types:__ Dipole; \n -__Paramters:__ Frequency in MHz; \n -__Output:__ Resonant frequency length;", inline=False)
            embedd.add_field(name="ERROR! rab!ban |[user_id]|[reason]|[delete Messages from last n days]", value="Bans a user. Only for Staff. Use n=0 for not deleting the messages.", inline=False)
            embedd.add_field(name="ERROR! rab!kick |[user_id]|[reason]", value="Kicks a user. Only for Staff.", inline=False)
            await message.channel.send(embed=embedd)

# Yeet a User
        elif message.content.startswith("rab!ban"):    # Doesn't Currently Work
            role = discord.utils.get(message.author.roles, name="Staff")
            banuserid = message.content.split("|")[1]
            try:
                banreason = message.content.split("|")[2]
            except:
                banreason = "Reason not specified."
            try:
                deleteMsgDays = message.content.split("|")[3]
            except:
                deleteMsgDays = 0
            if role in message.author.roles:
                if str(message.author.id) != banuserid:
                    try:
                        discord.User = client.get_user(int(banuserid))
                        await discord.User.ban(self, reason=banreason, delete_message_days=deleteMsgDays)
                        embedd = discord.Embed(title="`" + banuserid + "` got banned for `" + banreason + "` by " + str(message.author), colour=discord.Colour.red())
                        embedd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
                        await message.channel.send(embed=embedd)
                    except:
                        await message.channel.send("User not found")
                else:
                     await message.channel.send("You can't ban yourself bruh...")
            else:
                 await message.channel.send("You can't use that command!")

# Yeet a User but Not Forever
        elif message.content.startswith("rab!kick"):    # Doesn't Work Currently
            role = discord.utils.get(message.author.roles, name="Staff")
            kickuserid = message.content.split("|")[1]
            try:
                kickreason = message.content.split("|")[2]
            except:
                kickreason = "Reason not specified."
                
            if role in message.author.roles:
                if str(message.author.id) != kickuserid:
                    try:
                        discord.Member = client.get_user(int(kickuserid))
                        await discord.Member.kick(message, reason = kickreason)
                        embedd = discord.Embed(title="`" + kickuserid + "` got kicked for `" + kickreason + "` by " + str(message.author), colour=discord.Colour.blue())
                        embedd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
                    except:
                        await message.channel.send("User not found")
                else:
                     await message.channel.send("You can't kick yourself bruh...")
            else:
                 await message.channel.send("You can't use that command!")

# Calculate a Input
        elif message.content.startswith("rab!calc"):
            calculation_string = str(message.content)[9:]
            try:
                calculation_output = eval(calculation_string)
            except:
                calculation_output = "An error occured. Remember: you need to make a space between `calc` and your calculation."
            if len(str(calculation_output)) <= 2000:
                await message.channel.send(calculation_output)
            else:
                await message.channel.send("'Too Big' or something")

# Calculate an Antenna
        elif message.content.startswith("rab!antennacalc"):
            WhatToCalc=message.content.split(" ")[1]
            if WhatToCalc == "dipole" or WhatToCalc == "Dipole" or WhatToCalc == "dp": #dipole
                dipole_calc_string = str(message.content.split(" ")[2])
                dipole_calc_int = int(dipole_calc_string)
                try:
                    calc_output = (299.792458/dipole_calc_int)*50
                    calc_output_text = " Centimeters Per Pole"
                except:
                    calc_output = "[!] Error: "
                    calc_output_text = "An error occured while calculating"

            if len(str(calc_output)) <= 2000:
                await message.channel.send(str(calc_output)+calc_output_text)
            else:
                await message.channel.send("'Too Big' or something")

# Verification
        elif message.content.startswith("!verify"):
            role1 = discord.utils.get(message.guild.roles, name="Verified")
            role2 = discord.utils.get(message.guild.roles, name="Unverified")
            await message.author.add_roles(role1)
            await message.author.remove_roles(role2)
            await message.author.send("You Got verifed!")
            sleep(1)
            await message.delete()

        else:
            pass

##### END OF COMMANDS #####
##### MODERATION / LOGGING #####
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
        if str(after.author) != "Radio Astronomy Bot#0553" and before.author.bot == False:
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
        embedd.add_field(name="Member", value=member.mention, inline=False)
        embedd.add_field(name="Member ID:", value=str(member.id), inline=False)
        await channel.send(embed=embedd)
        await channel1.send("**" + str(member) + "** just left the server:slight_frown:")

    async def on_member_update(self, before, after):
        channel = client.get_channel(657875763546161153)
        if before.nick != after.nick and before.bot == False:
            embedd = discord.Embed(title="__**Nickname Changed**__", description="A Member has changed her/his Nickname.", colour=discord.Colour.dark_orange())
            embedd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
            embedd.add_field(name="Member:", value=before.mention, inline=False)
            embedd.add_field(name="Changed Nickname Before:", value=str(before.nick), inline=True)
            embedd.add_field(name="Changed Nickname After:", value=str(after.nick), inline=True)
            await channel.send(embed=embedd)
        else:
            pass

        if before.roles != after.roles:
            i1=0
            i2=0
            for i in before.roles:
                i1+=1
            for i in after.roles:
                i2+=1
            if i1-i2 > 0:
                change = "Removed"
                differnce=list(set(before.roles) - set(after.roles))
                emojie=":no_entry:"
            elif i1-i2 < 0:
                change = "Added"
                differnce=list(set(after.roles) - set(before.roles))
                emojie=":white_check_mark:"
            else:
                change = "Bruh ERROR"
            embedd = discord.Embed(title="Role " + change, description="A Member has changed her/his Roles.", colour=discord.Colour.dark_orange())
            embedd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
            embedd.add_field(name="Member:", value=before.mention, inline=False)
            embedd.add_field(name=emojie+change + " Role:", value=str(differnce), inline=False)
            await channel.send(embed=embedd)
        else:
            pass

    async def on_user_update(self, before, after):
        channel = client.get_channel(657875763546161153)
        if str(before.avatar_url) != str(after.avatar_url):
            embeddd = discord.Embed(title="__**Avatar Changed**__", description="A Member has changed her/his Avatar.", colour=discord.Colour.dark_orange())
            embeddd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
            embeddd.add_field(name="Member:", value=before.mention, inline=False)
            embeddd.set_thumbnail(url=after.avatar_url)
            embeddd.add_field(name="Changed Avatar Before (LINK DOESNT WORK):", value=str(before.avatar_url), inline=True)
            embeddd.add_field(name="Changed Avatar After:", value=str(after.avatar_url), inline=True)
            await channel.send(embed=embeddd)
        else:
            pass

        if str(before.name) != str(after.name):
            embeddd = discord.Embed(title="__**Username Changed**__", description="A Member has changed her/his Username.", colour=discord.Colour.dark_orange())
            embeddd.set_footer(text="Radio Astronomy Bot | made by Kaffeedor#0487 | 2020")
            embeddd.add_field(name="Member:", value=after.mention, inline=False)
            embeddd.set_thumbnail(url=after.avatar_url)
            embeddd.add_field(name="Changed Username Before:", value=str(before.name), inline=True)
            embeddd.add_field(name="Changed Username After:", value=str(after.name), inline=True)
            await channel.send(embed=embeddd)
        else:
            pass

    async def on_raw_reaction_add(self, payload):
        guild = client.get_guild(payload.guild_id)
        Member = guild.get_member(payload.user_id)
        user = client.get_user(payload.user_id)
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        exRAm = discord.utils.get(guild.roles, name="Experienced Radio Amateur")
        RAm = discord.utils.get(guild.roles, name="Radio Astronomy Amateur")
        RAb = discord.utils.get(guild.roles, name="Radio Astronomy Beginner")
        As = discord.utils.get(guild.roles, name="Astronomer")
        St = discord.utils.get(guild.roles, name="Stargazer")

        Rna = discord.utils.get(guild.roles, name="North America")
        Ras = discord.utils.get(guild.roles, name="Asia")
        Reu = discord.utils.get(guild.roles, name="Europe")
        Rsa = discord.utils.get(guild.roles, name="South America")
        Raao = discord.utils.get(guild.roles, name="Australia and Oceania")
        Raf = discord.utils.get(guild.roles, name="Africa")
        Ran = discord.utils.get(guild.roles, name="Antarctica")

        KytN = discord.utils.get(guild.roles, name="Kaffee's YT Notify")
        SN = discord.utils.get(guild.roles, name="Space News")

        if str(payload.channel_id) == "660914279729332224":
            if str(message.id) == "735422605569556592": # Astronomy and RA Roles
                if str(payload.emoji) == "🔴":
                    await Member.add_roles(exRAm)
                    try:
                        await Member.remove_roles(RAm)
                        await message.remove_reaction("🟠", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Rab)
                        await message.remove_reaction("🟡", Member)
                    except:
                        pass
                elif str(payload.emoji) == "🟠":
                    await Member.add_roles(RAm)
                    try:
                        await Member.remove_roles(exRAm)
                        await message.remove_reaction("🔴", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(RAb)
                        await message.remove_reaction("🟡", Member)
                    except:
                        pass
                elif str(payload.emoji) == "🟡":
                    await Member.add_roles(RAb)
                    try:
                        await Member.remove_roles(RAm)
                        await message.remove_reaction("🟠", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(exRAm)
                        await message.remove_reaction("🔴", Member)
                    except:
                        pass

                elif str(payload.emoji) == "🟢":
                    await Member.add_roles(As)
                    try:
                        await Member.remove_roles(St)
                        await message.remove_reaction("🔵", Member)
                    except:
                        pass
                elif str(payload.emoji) == "🔵":
                    await Member.add_roles(St)
                    try:
                        await Member.remove_roles(As)
                        await message.remove_reaction("🟢", Member)
                    except:
                        pass
                else:
                    pass

            elif str(message.id) == "735422606634778685": # Region Roles
                if str(payload.emoji) == "❤️":
                    await Member.add_roles(Rna)
                    try:
                        await Member.remove_roles(Reu)
                        await message.remove_reaction("🧡", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Ras)
                        await message.remove_reaction("💛", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Rsa)
                        await message.remove_reaction("💚", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Raf)
                        await message.remove_reaction("💙", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Raao)
                        await message.remove_reaction("💜", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Ran)
                        await message.remove_reaction("🤍", Member)
                    except:
                        pass

                elif str(payload.emoji) == "🧡":
                    await Member.add_roles(Reu)
                    try:
                        await Member.remove_roles(Rna)
                        await message.remove_reaction("❤️", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Ras)
                        await message.remove_reaction("💛", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Rsa)
                        await message.remove_reaction("💚", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Raf)
                        await message.remove_reaction("💙", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Raao)
                        await message.remove_reaction("💜", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Ran)
                        await message.remove_reaction("🤍", Member)
                    except:
                        pass

                elif str(payload.emoji) == "💛":
                    await Member.add_roles(Ras)
                    try:
                        await Member.remove_roles(Rna)
                        await message.remove_reaction("❤️", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Reu)
                        await message.remove_reaction("🧡", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Rsa)
                        await message.remove_reaction("💚", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Raf)
                        await message.remove_reaction("💙", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Raao)
                        await message.remove_reaction("💜", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Ran)
                        await message.remove_reaction("🤍", Member)
                    except:
                        pass

                elif str(payload.emoji) == "💚":
                    await Member.add_roles(Rsa)
                    try:
                        await Member.remove_roles(Rna)
                        await message.remove_reaction("❤️", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Reu)
                        await message.remove_reaction("🧡", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Ras)
                        await message.remove_reaction("💛", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Raf)
                        await message.remove_reaction("💙", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Raao)
                        await message.remove_reaction("💜", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Ran)
                        await message.remove_reaction("🤍", Member)
                    except:
                        pass

                elif str(payload.emoji) == "💙":
                    await Member.add_roles(Raf)
                    try:
                        await Member.remove_roles(Rna)
                        await message.remove_reaction("❤️", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Reu)
                        await message.remove_reaction("🧡", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Ras)
                        await message.remove_reaction("💛", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Rsa)
                        await message.remove_reaction("💚", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Raao)
                        await message.remove_reaction("💜", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Ran)
                        await message.remove_reaction("🤍", Member)
                    except:
                        pass

                elif str(payload.emoji) == "💜":
                    await Member.add_roles(Raao)
                    try:
                        await Member.remove_roles(Rna)
                        await message.remove_reaction("❤️", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Reu)
                        await message.remove_reaction("🧡", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Ras)
                        await message.remove_reaction("💛", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Rsa)
                        await message.remove_reaction("💚", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Raf)
                        await message.remove_reaction("💙", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Ran)
                        await message.remove_reaction("🤍", Member)
                    except:
                        pass

                elif str(payload.emoji) == "🤍":
                    await Member.add_roles(Ran)
                    try:
                        await Member.remove_roles(Rna)
                        await message.remove_reaction("❤️", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Reu)
                        await message.remove_reaction("🧡", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Ras)
                        await message.remove_reaction("💛", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Rsa)
                        await message.remove_reaction("💚", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Raf)
                        await message.remove_reaction("💙", Member)
                    except:
                        pass
                    try:
                        await Member.remove_roles(Raao)
                        await message.remove_reaction("💜", Member)
                    except:
                        pass
                   

            elif str(message.id) == "735422607779823617": # Other Roles
                if str(payload.emoji) == "☕":
                    await Member.add_roles(KytN)
                elif str(payload.emoji) == "🚀":
                    await Member.add_roles(SN)
                else:
                    pass

            else:
                pass

        else:
            pass

    async def on_raw_reaction_remove(self, payload):
        guild = client.get_guild(payload.guild_id)
        Member = guild.get_member(payload.user_id)
        user = client.get_user(payload.user_id)
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        exRAm = discord.utils.get(guild.roles, name="Experienced Radio Amateur")
        RAm = discord.utils.get(guild.roles, name="Radio Astronomy Amateur")
        RAb = discord.utils.get(guild.roles, name="Radio Astronomy Beginner")
        As = discord.utils.get(guild.roles, name="Astronomer")
        St = discord.utils.get(guild.roles, name="Stargazer")

        Rna = discord.utils.get(guild.roles, name="North America")
        Ras = discord.utils.get(guild.roles, name="Asia")
        Reu = discord.utils.get(guild.roles, name="Europe")
        Rsa = discord.utils.get(guild.roles, name="South America")
        Raao = discord.utils.get(guild.roles, name="Australia and Oceania")
        Raf = discord.utils.get(guild.roles, name="Africa")
        Ran = discord.utils.get(guild.roles, name="Antarctica")

        KytN = discord.utils.get(guild.roles, name="Kaffee's YT Notify")
        SN = discord.utils.get(guild.roles, name="Space News")

        if str(payload.channel_id) == "660914279729332224":
            if str(message.id) == "735422605569556592":
                if str(payload.emoji) == "🔴":
                    await Member.remove_roles(exRAm)

                elif str(payload.emoji) == "🟠":
                    await Member.remove_roles(RAm)

                elif str(payload.emoji) == "🟡":
                    await Member.remove_roles(RAb)

                elif str(payload.emoji) == "🟢":
                    await Member.remove_roles(As)

                elif str(payload.emoji) == "🔵":
                    await Member.remove_roles(St)

                else:
                    pass

            elif str(message.id) == "735422606634778685":
                if str(payload.emoji) == "❤️":
                    await Member.remove_roles(Rna)

                elif str(payload.emoji) == "🧡":
                    await Member.remove_roles(Reu)

                elif str(payload.emoji) == "💛":
                    await Member.remove_roles(Ras)

                elif str(payload.emoji) == "💚":
                    await Member.remove_roles(Rsa)

                elif str(payload.emoji) == "💙":
                    await Member.remove_roles(Raf)

                elif str(payload.emoji) == "💜":
                    await Member.remove_roles(Raao)

                elif str(payload.emoji) == "🤍":
                    await Member.remove_roles(Ran)

            elif str(message.id) == "735422607779823617":
                if str(payload.emoji) == "☕":
                    await Member.remove_roles(KytN)
                elif str(payload.emoji) == "🚀":
                    await Member.remove_roles(SN)
                else:
                    pass
            else:
                pass
        else:
            pass

##### END OF MODERATION / LOGGING #####

client = MyClient()
client.run("Token")