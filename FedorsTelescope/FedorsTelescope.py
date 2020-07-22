import discord
from time import sleep
from os import system
from os import remove

class MyClient(discord.Client):

    async def on_ready(self):
        print("I am Logged in. Beep Bob.")
        await client.change_presence(activity=discord.Game("ft!observe [sec] [nchan]"), status=discord.Status.online)

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith("ft!observe"):
            # 2343.75; 1171.875; 4687, 5
            obst = message.content.split(" ")[1]
            try:
                nchan = message.content.split(" ")[2]
            except:
                nchan=""

            try:
                remove('observation.dat')
                remove('plot.png')
            except OSError:
                pass
            await message.channel.send("Observation Starting Now!")
            await client.change_presence(activity=discord.Game("Observing for " + str(obst) + " sec"), status=discord.Status.online)

            if nchan == "":
                nchan="512"
            else:
                pass

            if nchan == "512":
                system("python top_block.py --c-freq=1.420e9 --samp-rate=2.4e6 --nchan=512 --nbin=4688 --obs-time="+str(obst))
                system("python plot_hi.py freq=1420e6 samp_rate=2.4e6 nchan=512 nbin=4688")
            elif nchan == "1024":
                system("python top_block.py --c-freq=1.420e9 --samp-rate=2.4e6 --nchan=1024 --nbin=2344 --obs-time="+str(obst))
                system("python plot_hi.py freq=1.420e9 samp_rate=2.4e6 nchan=1024 nbin=2344")
            elif nchan == "2048":
                system("python top_block.py --c-freq=1.420e9 --samp-rate=2.4e6 --nchan=2048 --nbin=1172 --obs-time="+str(obst))
                system("python plot_hi.py freq=1.420e9 samp_rate=2.4e6 nchan=2048 nbin=1172")
            else:
                await message.channel.send("(You need to use `512`, `1024` or `2048` for `nchan`!)")

            sleep(2)
            print("observation done")
            try:
                await message.channel.send("Your Observation is here. Fresh and Tasty!", file=discord.File("plot.png"))
            except:
                await message.channel.send("Couldn't find `plot.png` (or some other random error?!)")
            await client.change_presence(activity=discord.Game("ft!observe [sec] [nchan]"), status=discord.Status.online)

        else:
            pass

#        if message.content.startswith("ft!cancel"):    # Doesn't Work Currently
#            system("pkill -f top_block.py")

#        else:
#            pass

client = MyClient()
client.run("TOKEN")