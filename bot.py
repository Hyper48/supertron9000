import discord
import os
import random
from discord.ext import commands
from itertools import cycle
import json

client = commands.Bot(command_prefix = 's!')
client.remove_command('help')


@client.command(pass_context=True)
async def help(ctx):
	author = ctx.message.author

	embed = discord.Embed(
		colour = discord.Colour.blue()
	)

	embed.set_author(name='These are all the commands for SuperBOT')

	embed.add_field(name='tiktok', value="Sends a link to SuperDEAD's tiktok!", inline=False)

	embed.add_field(name='twitch', value="Sends a link to SuperDEAD's Twitch channel!", inline=False)

	embed.add_field(name='ig (insta and instagram work too)', value="Sends a link to SuperDEAD's Instagram profile!", inline=False)
	
	embed.add_field(name='discordinvite', value='Sends a server invite that can be sent to others!', inline=False)

	embed.add_field(name='botcode', value='Sends the the bots code. It is public to everyone', inline=False)

	embed.set_footer(text="Developed by Hyper™#0999")







	await ctx.send(embed=embed)


# tik tok command
@client.command()
async def tiktok(ctx):
	
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)

	embed.add_field(name="Here is a link to SuperDEAD's Tik Tok", value= '@superdeadtk - https://www.tiktok.com/@superdeadtk', inline=False)

	await ctx.send(embed=embed)


# twitch command
@client.command()
async def twitch(ctx):
	
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)

	embed.add_field(name="Here is a link to SuperDEAD's Twitch channel!", value='SuperDEADTW- https://www.twitch.tv/superdeadtw', inline=False)

	await ctx.send(embed=embed)


# ig command
@client.command(aliases=['insta', 'instagram'])
async def ig(ctx):
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)

	embed.add_field(name="Here is a link to SuperDEAD's Instagram profile!", value='SuperDEADTW- https://www.twitch.tv/superdeadtw', inline=False)

	await ctx.send(embed=embed)


# invite command
@client.command()
async def discordinvite(ctx):
	await ctx.send(f'This is a permanent invite link to this server!!: https://discord.gg/UTerh9V')


# code command
@client.command()
async def botcode(ctx):
	await ctx.send(f'This bot is developed by <@492830898606178314> (Hyper™#0999). It is open source! Feel free to use the code. The code can be found on this Github page: https://github.com/Hyper48/SuperBOT')






client.run(os.environ['DISCORD_TOKEN'])






# If you are reading this, have a great day cutie :)