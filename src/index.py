from functools import reduce

import discord
from discord.ext import commands

import re
from urllib import parse, request

import random

from jeer_list import diego, emilio, jojo, dani, josu, kris
from wisdom import PHRASES

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

bot = commands.Bot(command_prefix='>', description='This is a colombian bot')

def select_swear(user): 
    num = random.randint(0,len(user)-1)
    return user[num]

@bot.event
async def on_message(message):
    
    if ("dame" in message.content.lower() or "quiero" in message.content.lower()) and "consejo" in message.content.lower():
        await message.channel.send(select_swear(PHRASES))
        await bot.process_commands(message)

    elif "secreto del dani" in message.content.lower():
        with open('.\\images\\288149984_1226690144827030_1944250487301843159_n.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
        f.close()

    elif "diego" in message.content.lower():
        await message.channel.send(select_swear(diego))
        await bot.process_commands(message)

    elif "emilio" in message.content.lower():
        await message.channel.send(select_swear(emilio))
        await bot.process_commands(message)

    elif "jojo" in message.content.lower():
        await message.channel.send(select_swear(jojo))
        await bot.process_commands(message)
        
    elif "dani" in message.content.lower():
        await message.channel.send(select_swear(dani))
        await bot.process_commands(message)
    
    elif "josu" in message.content.lower():
        await message.channel.send(select_swear(josu))
        await bot.process_commands(message)
    
    elif "kris" in message.content.lower() or "cris" in message.content.lower():
        await message.channel.send(select_swear(kris))
        await bot.process_commands(message)

    elif "que" == message.content.lower()[-3:]:
        await message.channel.send("so")
        await bot.process_commands(message)
    
    elif "so" == message.content.lower()[-3:]:
        await message.channel.send("rra")
        await bot.process_commands(message)
    
    elif "rra" == message.content.lower()[-3:]:
        await message.channel.send("sos")
        await bot.process_commands(message)
    
    elif "sos" == message.content.lower()[-3:]:
        await message.channel.send("vos")
        await bot.process_commands(message)
    
    elif "women" in message.content.lower():
        await message.channel.send('https://youtu.be/e9mVfv3b-4E')
    
    elif "bot" in message.content.lower() and "aweonao" in message.content.lower():
        await message.channel.send("mas respeto negro de mierda")
        await bot.process_commands(message)

    elif "su lol" in message.content.lower() or "sulol" in message.content.lower():
        await message.channel.send("Deja el vicio weon.")
    
    elif "$wa" in message.content.lower():
        await message.channel.send("Virgen")
    

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Pornito",url='https://www.twitch.tv/diegojudio'))
    print("Ready to go.")

bot.run('OTg3MjMyMjg4NjQxMjY5ODIw.GnBq9e.2sBvKON6poU_nUFH2QT401IwKQvzWHqp51VtTE')