import discord
#pip install discord
import asyncio
#pip install asyncio
import os
import requests
#pip install requests
import re

import random

from bs4 import BeautifulSoup
#pip install bs4
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

articles_array = []

url = 'https://www.10000recipe.com/'
recipeurl = 'https://www.10000recipe.com/recipe/'
recipeurlend = ''

async def remove_html(sentence) :
	sentence = re.sub('(<([^>]+)>)', '', sentence)
	return sentence

@bot.event
async def on_ready():
    print('Loggend in Bot: ', bot.user.name)
    print('Bot id: ', bot.user.id)
    print('connection was succesful!')
    print('=' * 30)

@bot.command(name='안녕')
async def hello(ctx):
    my_channel = ctx.channel.guild.get_channel(1166754990900117536)
    await ctx.channel.send("{}, 반갑습니다!".format(ctx.author.mention))

@bot.command(name='정보')
async def information(ctx):
    my_channel = ctx.channel.guild.get_channel(1166754990900117536)
    embed = discord.Embed(title="testingbot 정보", description="", color=0x9933FF)
    embed.set_thumbnail(url="")
    embed.add_field(name="사이트", value="만개의 레시피 사이트로 이동할 수 있습니다.", inline=False)
    embed.add_field(name="레시피", value="랜덤한 음식 레시피를 볼 수 있습니다.", inline=False)
    embed.add_field(name="비건", value="랜덤한 비건 음식 레시피를 볼 수 있습니다.", inline=False)
    embed.add_field(name="...", value="개발중...", inline=False)
    embed.add_field(name="...", value="개발중...", inline=False)
    embed.add_field(name="???", value="easter egg", inline=False)
    embed.set_footer(text="Bot Made by YOUR NAME", icon_url="")

    await ctx.channel.send(embed=embed)

@bot.command(name='사이트')
async def go_to_site(ctx):
    my_channel = ctx.channel.guild.get_channel(1166754990900117536)
    await ctx.channel.send("만개의 레시피로 이동하기!\n{}".format(url))

@bot.command(name='레시피')
async def go_to_site(ctx):
    my_channel = ctx.channel.guild.get_channel(1166754990900117536)
    await ctx.channel.send("레시피 찾는 중...")

    recipe=random.randint(1,15)

    if recipe == 1:
        recipeurlend = recipeurl + '6845172'
    elif recipe == 2:
        recipeurlend = recipeurl + '6881450'
    elif recipe == 3:
        recipeurlend = recipeurl + '6901938'
    elif recipe == 4:
        recipeurlend = recipeurl + '6836718'
    elif recipe == 5:
        recipeurlend = recipeurl + '6883026'
    elif recipe == 6:
        recipeurlend = recipeurl + '6832027'
    elif recipe == 7:
        recipeurlend = recipeurl + '6905422'
    elif recipe == 8:
        recipeurlend = recipeurl + '6928043'
    elif recipe == 9:
        recipeurlend = recipeurl + '3553637'
    elif recipe == 10:
        recipeurlend = recipeurl + '6926532'
    elif recipe == 11:
        recipeurlend = recipeurl + '5269045'
    elif recipe == 12:
        recipeurlend = recipeurl + '6955248'
    elif recipe == 13:
        recipeurlend = recipeurl + '6908683'
    elif recipe == 14:
        recipeurlend = recipeurl + '6847652'
    elif recipe == 15:
        recipeurlend = recipeurl + '6952503'

    await asyncio.sleep(1)

    await ctx.channel.send("랜덤 레시피!\n{}".format(recipeurlend))

@bot.command(name='비건')
async def go_to_site(ctx):
    my_channel = ctx.channel.guild.get_channel(1166754990900117536)
    await ctx.channel.send("비건 레시피 찾는 중...")

    recipe=random.randint(1,10)

    if recipe == 1:
        recipeurlend = recipeurl + '6912734'
    elif recipe == 2:
        recipeurlend = recipeurl + '7003487'
    elif recipe == 3:
        recipeurlend = recipeurl + '7012184'
    elif recipe == 4:
        recipeurlend = recipeurl + '6847506'
    elif recipe == 5:
        recipeurlend = recipeurl + '6872384'
    elif recipe == 6:
        recipeurlend = recipeurl + '6887806'
    elif recipe == 7:
        recipeurlend = recipeurl + '6829316'
    elif recipe == 8:
        recipeurlend = recipeurl + '6835002'
    elif recipe == 9:
        recipeurlend = recipeurl + '6891642'
    elif recipe == 10:
        recipeurlend = recipeurl + '6929166'

    await asyncio.sleep(1)

    await ctx.channel.send("랜덤 비건 레시피!\n{}".format(recipeurlend))



bot.run('TOKEN')