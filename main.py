import discord

TOKEN = "BOT_TOKEN"
client = discord.Client()


help_text = ''''''


def help_command(message):
    message.channel.send(help_text)


def choose_game_command(message):
    message.channel.send('Напишите название игры')


def func_name_3():
    # description of third func
    pass


# creating global collections used for messages parsing
KEYWORD_COMMANDS = {'помощь': help_command,
                    'help': help_command,
                    'справка': help_command,
                    'game': choose_game_command,
                    'игра': choose_game_command}


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
    global KEYWORD_COMMANDS
    if message.author == client.user:
        return
    for word in KEYWORD_COMMANDS.keys():
        if word in message.content.lower():
            temp_func_name = KEYWORD_COMMANDS[word]
            temp_func_name(message)


# launching
client.run(TOKEN)
