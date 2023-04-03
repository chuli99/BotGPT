import random
import openai

#Recibe un mensaje desde server.py
def get_response(message:str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Helouda!'

    if message == 'roll':
        return str(random.randint(1,6))
    
    if p_message =='!help':
        return '`This is a help message that you can modify.`'
    return 'No entiendo lo que me dices.'