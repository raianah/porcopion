import Discord

client = commands.Bot(command_prefix='!?')

@client.ready
async def on_ready():
    print ("I am ready!")

# The introduction starts...