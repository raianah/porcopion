import discord
from discord.ext import commands, tasks
import asyncio
import datetime


client = commands.Bot(command_prefix = '?', case_insensitive=True)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Documentation | !help p<num>."))
    print('This repository is for documentation only.')
    
@client.command()
async def hello(ctx):
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
    embed.add_field(name='\u200b', value=f'Hello there, {ctx.author.mention}!)
    embed.set_footer(text='Giving you a warm cup of coffee to start up your day!')
    await ctx.send(embed=embed)

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(
        title="📬 | Help Command",
        description='This is the front page of help command.\n>help <P(num)> for more info.',
        timestamp = datetime.datetime.utcnow(),
        color = 0x855988
    )
    em.add_field(name='\u200b', value='👉 | **Page 1 (P1)**: Entertainment commands.', inline=False)
    em.add_field(name='\u200b', value='👉 | **Page 2 (P2)**: Mini-game commands.', inline=False)
    em.add_field(name='\u200b', value='👉 | **Page 3 (P3)**: Suggestion commands.', inline=False)
    em.add_field(name='\u200b', value='👉 | **Page 4 (P4)**: Moderation commands.', inline=False)
    em.set_footer(text=f'• Twilight • {ctx.author.name} • >help p1 for next page', icon_url="https://cdn.discordapp.com/attachments/831412988111487017/836129293070499900/20210426_140531_0000.png")
    await ctx.send(embed=em)

@help.command(aliases=['P1'])
async def p1(ctx):
    em = discord.Embed(
        title = '🎉 | Page 1/4 (ENTERTAINMENT COMMANDS)',
        description = 'Here is the lists of available entertainment commands.',
        timestamp = datetime.datetime.utcnow(),
        color = 0x483475
    )
    em.add_field(name='Ask *(ask)*', value='Asks the bot, and gives random answers!', inline=False)
    em.add_field(name='Ask 2 *(ask2)*', value='Asks the bot, and gives random answers (PART 2)!', inline=False)
    em.add_field(name='Never Have I Ever *(nhie)*', value='Never have you ever???', inline=False)
    em.add_field(name='Quiz *(qz)*', value='Answer the questions, learn more about it.', inline=False)
    em.add_field(name='Riddle *(rdl)*', value='Sends a riddle, and answer it on your own! **Answers not included!**', inline=False)
    em.add_field(name='Tell me a joke! *(tmaj)*', value='Asks the bot, and gives lists of pure cringe jokes and 100% pure dad jokes!', inline=False)
    em.add_field(name='Topic *(tpc)*', value='Gives random topic.', inline=False)
    em.add_field(name='Would You Rather *(wyr)*', value='Gives two ~~useless~~ choices to choose.', inline=False)
    em.set_footer(text=f'• Twilight • {ctx.author.name} • >help p3 for next page ', icon_url="https://cdn.discordapp.com/attachments/831412988111487017/836129293070499900/20210426_140531_0000.png")
    await ctx.send(embed=em)

@help.command(aliases=['P2'])
async def p2(ctx):
    em = discord.Embed(
        title = '🎮 | Page 2/4 (MINI-GAME COMMANDS)',
        description = 'Here is the lists of available mini-game commands.',
        timestamp = datetime.datetime.utcnow(),
        color = 0x2B2F77
    )
    em.add_field(name='Coinflip *(cnf)*', value='Test your luck, flip the coin!', inline=False)
    em.add_field(name='Pick a Number *(pcn)*', value='Find your lucky number. Test your luck. Maximum number: **300**.', inline=False)
    em.add_field(name='Rolldice *(rdc)*', value='Roll the dice, hit the number you want.', inline=False)
    em.add_field(name='Double Dice *(rdc2)*', value='Double the dice, X2 the results!', inline=False)
    em.set_footer(text=f'• Twilight • {ctx.author.name} • >help p4 for next page ', icon_url="https://cdn.discordapp.com/attachments/831412988111487017/836129293070499900/20210426_140531_0000.png")
    await ctx.send(embed=em)

@help.command(aliases=['P3'])
async def p3(ctx):
    em = discord.Embed(
        title = '💡 | Page 3/4 (SUGGESTION COMMANDS)',
        descriptipn = 'Here is the lists of available suggestion commands.',
        timestamp = datetime.datetime.utcnow(),
        color = 0x141852
    )
    em.add_field(name='Suggest *(sgg)*', value='Add spice to the bot by suggesting to us. We would like to hear your great suggestion.', inline=False)
    em.add_field(name='Vote Poll *(vtpl)*', value='Make your opinion count. Let the members vote, and the administrators of your server will do the rest.', inline=True)
    em.add_field(name='Topic Suggestion *(sggtpc)*', value='Give your very own topic to be discussed in global terms, or in private terms. You decide.', inline=True)
    em.add_field(name='WYR Suggestion *(sggwyr)*', value='Having a hard time to choose between two terms/decisions? Count us in.', inline=True)
    em.add_field(name='ASK Suggestion *(sggask)*', value='This suggestion is exclusive for goofy answers for `>ask` & `>ask2` commands.', inline=True)
    em.add_field(name='TMAJ Suggestion *(sggtmaj)*', value="Give your most cringe dad joke you've ever heard.", inline=True)
    em.add_field(name='Anonymous Suggestion *(sgganon)*', value='Wanting to share your thoughts without revealing your identity to anyone including us? Well this is it.', inline=True)
    em.set_footer(text=f'• Twilight • {ctx.author.name} • >help p5 for next page ', icon_url="https://cdn.discordapp.com/attachments/831412988111487017/836129293070499900/20210426_140531_0000.png")
    await ctx.send(embed=em)

@help.command(aliases=['P4'])
async def p4(ctx):
    em = discord.Embed(
        title = '👮 | PAGE 4/4 (MODERATION & UTILITY COMMANDS)',
        description = 'Here is the lists of available utility commands.',
        timestamp = datetime.datetime.utcnow(),
        color = 0x375597
    )
    em.add_field(name='AFK *(afk)*', value='Gives you AFK Status, and muted until the given duration *(`>afk <number (s/m/h/d)>`) please input space between the number and the denominator*.', inline=False)
    em.add_field(name='Ping *(pn)*', value="Sends the bot current latency. Want to see how lag this bot is?", inline=False)
    em.add_field(name='Clear *(clr)*', value='Clears and removes recent messages *(default: 3)*.', inline=False)
    em.add_field(name='Permamute *(mtp)*', value='Mute members indefinitely.', inline=False)
    em.add_field(name='Timed Mute *(mt)*', value='Mute members with given time. *(`>mute <member> <number> <space> <s/m/h/d>`) please input space between the number and the denominator.*', inline=False)
    em.add_field(name='Unmute *(umt)*', value='Un-mute members earlier than the given time.', inline=False)
    em.set_footer(text=f'• Twilight • {ctx.author.name} • >help p7 for next page ', icon_url="https://cdn.discordapp.com/attachments/831412988111487017/836129293070499900/20210426_140531_0000.png")
    await ctx.send(embed=em)
    
client.run('token')
