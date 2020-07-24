# Radio Astronomy Bot
Radio Astronomy Bot is a Discord Bot with powerful Moderation tools and some neat Radio Astronomy commands.
There is also the Fedor's Telescope Bot which controls my Radio Telescope.
Fedor's Telescope Bot is powered with [VIRGO](https://github.com/0xCoto/VIRGO) by [0xCoto](https://github.com/0xCoto).
This bot is maintained and is operational on the [Radio Astronomy and Space](https://disboard.org/server/657857708644499458) Discord Server.

### Disclaimer: Current Security Issue
The `rab!calc` command currently will interperit anything that is put into it. This will be fixed soon. If you do not want this, dig in and remove it yourself. The part you want to remove is in `/RAB/rab.py/` and the code you want to remove is:
```python
elif message.content.startswith("rab!calc"):
    calculation_string = str(message.content)[8:]
    calculation_output = eval(calculation_string)

    if len(str(calculation_output)) <= 2000:
        await message.channel.send(calculation_output)
    else:
        await message.channel.send("'Too Big' or something")
    else:
        pass
```
### Disclaimer: Bot Optimized for a Specific Server ([Radio Astronomy and Space](https://disboard.org/server/657857708644499458)):
This Bot *WILL NOT WORK* if you just copy the code and change the Token! You need to change the Roles and Channels to make it work!
