# author zod
# date 11/11/2019

import os
from os import listdir, remove
from os.path import join, isfile
import json
import time
import discord
import random
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Game
from itertools import cycle

with open("config.json") as json_data_file:
    data = json.load(json_data_file)

bot = commands.Bot(command_prefix=data["prefix"])
bot.remove_command("help")


async def change_status():
    await bot.wait_until_ready()
    msgs = cycle(data["status"])
    while not bot.is_closed():
        current_status = next(msgs)
        await bot.change_presence(status=discord.Status.do_not_disturb,
                                  activity=discord.Activity(type=discord.ActivityType.playing, name=current_status))
        await asyncio.sleep(20)


@bot.event
async def on_ready():
    print('--------------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('--------------')
    print('Current servers:')
    for guild in bot.guilds:
        print(guild.name)
    print('--------------')


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        colour=discord.Colour.blue()
    )
    embed.set_author(name="Yui Commands", icon_url=bot.user.avatar_url)

    embed.add_field(name="$hug", value="This command allows you to hug a friend!\n"
                    "Example: `$hug @user`", inline=False)

    embed.add_field(name="$kiss", value="This command allows you to kiss someone you like :3!\n"
                    "Example: `$kiss @user`", inline=False)

    embed.add_field(name="$pat", value="This command allows you to pat a friend!\n"
                    "Example: `$pat @user`", inline=False)

    embed.add_field(name="$slap", value="This command allows you to slap a friend!\n"
                    "Example: `$slap @user`", inline=False)

    embed.add_field(name="$yui", value="This command allows you to see random pics of yui!\n"
                    "Example: `$clear`", inline=False)

    embed.add_field(name="$echo", value="This command allows you to make the bot say what you say!\n"
                    "Example: `$echo message`", inline=False)

    embed.add_field(name="$iplookup", value="This command allows you to lookup someone's location with an ip!\n"
                    "Example: `$iplookup 127.0.0.1`", inline=False)

    await ctx.send(embed=embed)

for filename in [f for f in listdir('cogs') if isfile(join('cogs', f))]:
    if filename[-3:] == '.py':
        bot.load_extension('cogs.' + filename[:-3])

bot.loop.create_task(change_status())
bot.run(data["token"])
