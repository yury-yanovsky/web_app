import discord
import requests



TOKEN = "BOT_TOKEN"
client = discord.Client()


def func_name():
    pass


def func_name_2():
    pass


def func_name_3():
    pass


KEYWORDS = ['1', '2', '3']
KEYWORD_COMMANDS = {'1': func_name,
                    '2': func_name_2,
                    '3': func_name_3}


@client.event
async def on_ready():
    print(f'{client.user} подключен к Discord!')
    for guild in client.guilds:
        print(
            f'{client.user} подключились к чату:\n'
            f'{guild.name}(id: {guild.id}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for word in KEYWORDS:
        if word in message.content.lower():
            temp_func_name = KEYWORD_COMMANDS[word]
            temp_func_name()


client.run(TOKEN)
