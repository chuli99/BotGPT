import random
import openai
import os
from dotenv import load_dotenv

#Recibe un mensaje desde server.py
def get_response(message:str) -> str:
    p_message = message.lower()

    if p_message[:4] == '!gpt':
        if p_message[5:] == 'hello': 
            return str('Hello there')
        if message[5:] == 'roll':
            return str(random.randint(1,6))
        
        if p_message[5:] =='help':
            return '`El comando a utilizar es !gpt .`'
        
        else:
            #Cargo mi api_key de chatgpt
            load_dotenv()
            api_key = os.getenv('OPENAI_API_KEY')
            openai.api_key = api_key

            #Asigno lo ingresado por mensaje de discord como prompt
            prompt = str(p_message[5:]) 
            
            response = openai.Completion.create(engine="text-davinci-003",prompt=prompt,max_tokens=2048)
            return (response.choices[0].text)
    