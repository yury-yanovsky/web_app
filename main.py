import discord

TOKEN = "BOT_TOKEN"
client = discord.Client()


def func_name():
    # description of first func
    pass


def func_name_2():
    # description of second func
    pass


def func_name_3():
    # description of third func
    pass


# creating global collections used for messages parsing
KEYWORDS = ['1', '2', '3']
KEYWORD_COMMANDS = {'1': func_name,
                    '2': func_name_2,
                    '3': func_name_3}


# boot function
@client.event
async def on_ready():
    print(f'{client.user} подключен к Discord!')
    for guild in client.guilds:
        print(
            f'{client.user} подключились к чату:\n'
            f'{guild.name}(id: {guild.id}')


# messages parsing
@client.event
async def on_message(message):
    global KEYWORDS, KEYWORD_COMMANDS
    if message.author == client.user:
        return
    for word in KEYWORDS:
        if word in message.content.lower():
            temp_func_name = KEYWORD_COMMANDS[word]
            temp_func_name()


# launching
client.run(TOKEN)
