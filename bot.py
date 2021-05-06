import discord
from discord.ext import commands, tasks
import asyncio
import datetime


client = commands.Bot(command_prefix = '?', case_insensitive=True)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Readthedocs | !help p<num>."))
    print('This code is for documentation only.')



@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(
        title="📬 | Help Command",
        description='This is the front page of help command.\n>help <P(num)> for more info.',
        timestamp = datetime.datetime.utcnow(),
        color = 0x855988
    )
    em.add_field(name='\u200b', value='👉 | **Page 1 (P1)**: Latest updates to the bot.', inline=False)
    em.add_field(name='\u200b', value='👉 | **Page 2 (P2)**: Entertainment commands.', inline=False)
    em.add_field(name='\u200b', value='👉 | **Page 3 (P3)**: Mini-game commands.', inline=False)
    em.add_field(name='\u200b', value='👉 | **Page 4 (P4)**: Suggestion commands.', inline=False)
    em.add_field(name='\u200b', value='👉 | **Page 5 (P5)**: Invite links.', inline=False)
    em.add_field(name='\u200b', value='👉 | **Page 6 (P6)**: Moderation commands (soon).', inline=False)
    em.add_field(name='\u200b', value='👉 | **Page 7 (P7)**: Suggestion results', inline=False)
    em.add_field(name='\u200b', value='👉 | **Page 8 (total)**: Total commands available for this patch.', inline=False)
    em.set_footer(text=f'• Twilight • {ctx.author.name} • >help p1 for next page', icon_url="https://cdn.discordapp.com/attachments/831412988111487017/836129293070499900/20210426_140531_0000.png")
    await ctx.send(embed=em)

@help.command(aliases=['P1'])
async def p1(ctx):
    em = discord.Embed(
        title='💾 | Page 1/8 (PATCH NOTES 0.1.0)',
        description='Here is the current patch, and some noticeable updates to the bot.',
        timestamp = datetime.datetime.utcnow(),
        color = 0x6B4984
    )
    em.set_thumbnail(url='https://cdn.discordapp.com/attachments/831412988111487017/836150693428592640/W_Y_R_2___9.png')
    em.add_field(name='#1', value='Added `permamute`, `unmute`, `mute`, `kick` & `ban` commands in preparation for moderator opening.', inline=False)
    em.add_field(name='#2', value='Added AFK command which acts like mute command but for yourself only.', inline=False)
    em.add_field(name='#3', value='Added 40+ numbers in `pickanum` command.', inline=False)
    em.add_field(name='#4', value='Added profanity filter.', inline=False)
    em.add_field(name='#5', value="Added 10 new topics, 10 new wyr's, 10 new riddles, 10 new tmaj's, and 10 new answers from both `>ask` & `>ask2`.", inline=False)
    em.add_field(name='#6', value='Added aliases for lesser inputs. Please be guided by using the `help P(num)` command.', inline=False)
    em.add_field(name='#7', value='Truth or Dare command has been removed.', inline=False)
    em.add_field(name='#8', value='Added `quiz` command with `15` questions each with multiple choices. You decide which is right or wrong.', inline=False)
    em.set_footer(text=f'• Twilight • {ctx.author.name} • >help p2 for next page ', icon_url="https://cdn.discordapp.com/attachments/831412988111487017/836129293070499900/20210426_140531_0000.png")
    await ctx.send(embed=em)

@help.command(aliases=['P2'])
async def p2(ctx):
    em = discord.Embed(
        title = '🎉 | Page 2/8 (ENTERTAINMENT COMMANDS)',
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

@help.command(aliases=['P3'])
async def p3(ctx):
    em = discord.Embed(
        title = '🎮 | Page 3/8 (MINI-GAME COMMANDS)',
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

@help.command(aliases=['P4'])
async def p4(ctx):
    em = discord.Embed(
        title = '💡 | Page 4/8 (SUGGESTION COMMANDS)',
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

@help.command(aliases=['P5'])
async def p5(ctx):
    em = discord.Embed(
        title = '✉️ | PAGE 5/8 ~~(USELESS PAGE)~~ (INVITE LINKS)',
        description = 'Support Jukebox, Vinyl, and Twilight! Vote them.',
        timestamp = datetime.datetime.utcnow(),
        color = 0x070B34
    )
    em.add_field(name='Jukebox', value='Join Jukebox in your server [here](https://top.gg/bot/829596382977327146).', inline=False)
    em.add_field(name='Twilight', value='Soon.', inline=False)
    em.set_footer(text=f'• Twilight • {ctx.author.name} • >help p6 for next page ', icon_url="https://cdn.discordapp.com/attachments/831412988111487017/836129293070499900/20210426_140531_0000.png")
    await ctx.send(embed=em)

@help.command(aliases=['P6'])
async def p6(ctx):
    em = discord.Embed(
        title = '👮 | PAGE 6/8 (MODERATION & UTILITY COMMANDS)',
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

@help.command(aliases=['P7'])
async def p7(ctx):
    em = discord.Embed(
        title = '📩 | PAGE 7/8 (SUGGESTION RESULTS)',
        description = 'See all reviewed suggestions here.',
        timestamp = datetime.datetime.utcnow(),
        color = 0xfd5e53
    )
    em.set_footer(text=f'• Twilight • {ctx.author.name} • >help total for next page ', icon_url="https://cdn.discordapp.com/attachments/831412988111487017/836129293070499900/20210426_140531_0000.png")
    em.add_field(name='\u200b', value='┏━━━━━━━━━━༻❁༺━━━━━━━━━━┓', inline=False)
    em.add_field(name='Approved Suggestions:', value='**0**', inline=True)
    em.add_field(name='Declined Suggestions:', value='**0**', inline=True)
    em.add_field(name='┗━━━━━━━━━━༻❁༺━━━━━━━━━━┛', value='\u200b', inline=False)
    em.add_field(name='\u200b', value='\u200b')
    em.add_field(name='\u200b', value='┏━━━━━━━━━━༻❁༺━━━━━━━━━━┓', inline=False)
    em.add_field(name='#1', value='N/A.', inline=False)
    em.add_field(name='#2', value='N/A.', inline=False)
    em.add_field(name='#3', value='N/A.', inline=False)
    em.add_field(name='┗━━━━━━━━━━༻❁༺━━━━━━━━━━┛', value='\u200b', inline=False)
    await ctx.send(embed=em)

@help.command()
async def total(ctx):
    em = discord.Embed(
        title = '👉 | PAGE 8/8 (TOTAL COMMANDS)',
        description = 'This page is nothing but total commands. Seriously.',
        timestamp = datetime.datetime.utcnow(),
        color = 0xc57893
    )
    em.add_field(name='\u200b', value='**Total Commands:** *35!*')
    em.set_footer(text=f'• Twilight • {ctx.author.name} • this is the last page ', icon_url='')
    await ctx.send(embed=em)