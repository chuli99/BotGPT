import os 
from dotenv import load_dotenv

import discord
import responses





async def send_message(message,user_message,user,is_private):
    try:
        #Trae como respuesta lo codeado en response
        response = responses.get_response(user_message)
        
        #Solucion de problema ya que al llamar a response y no usar un comando, daba problemas.
        if response != None:
            await message.author.send(f"{'@'}{user[:-5]}{response}") if is_private else await message.channel.send(f"{'@'}{user[:-5]}{response}")
    except Exception as e:
        print(e)


def run_discord_bot():
    load_dotenv()
    #Obtenemos token
    TOKEN = os.getenv('DISCORD_TOKEN')
    #Por politicas de discord es necesario (investigar mas)
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user}is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message,user_message,username,is_private=True)
        else:
            await send_message(message,user_message,username,is_private=False)

    client.run(TOKEN)