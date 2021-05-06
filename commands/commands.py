import discord
import random
from discord.ext import commands, tasks
from discord import DMChannel
from discord.ext.commands import MissingPermissions
import pafy
import logging
import datetime
import asyncio
from random import choice

client = commands.Bot(command_prefix = "!?", case_insensitive=True)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="35 Commands | >help for commands."))
    print('Commands are here.')

@client.command(aliases=['aliases_are_here'])
async def command(ctx):
    await ctx.send(f"**{ctx.author.name}:** You are!")

@client.event
async def on_message(message):
    profanity = ['input', 'profanity words', 'here', 'with', 'single or double quotation', 'marks and commas', 'for separation of words']
    for profanity in profanity:
        if profanity in message.content:
            await message.delete()
            await message.channel.send("Oops, you said the forbidden word!")
        else:
            await client.process_commands(message)

@client.command()
async def random(ctx):
    responses = ["Put sentences in here",
                 "Put atleast 10 choices to prevent from repeating the same response",
                 "Do not forget to put comma after each response",
                 "Use double quotations if you are using single quotation as 'apostrophe'",
                 "*Markdowns* **work** ~~here~~"]
    await ctx.send(f"{random.choice(responses)}")

@client.group(invoke_without_command=True)
async def group(ctx):
    await ctx.send("This is the main page for grouped commands.")

@group.command(aliases=['you can put the command instead of client'])
async def group2(ctx):
    await ctx.send("It should not be identical as the other commands!")

@group.command(aliases=['we are using embeds now'])
async def group3(ctx):
    embed = discord.Embed(title='Put title here', description='Put description here') # timestamp = datetime... / you can use 0x(hex codes), or just use discord colors by inputting discord.Color.color.
    embed.add_field(name='Put name here', value='Short description, or whatever fits your socks.')
    embed.add_field(name='\u200b', value='the name will appear as blank.')
    embed.add_field(name='\u200b', value='please refer to discord.py documentation for full commands.')

client.run('token')