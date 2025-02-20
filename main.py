from dotenv import load_dotenv
from openai import OpenAI
from colorama import Fore
import warnings
import os


warnings.filterwarnings("ignore")

# LOAD ENV VARIABLES
load_dotenv()

# Load the model
stringValue=os.getenv("DEEPSEEK_R1_API_KEY")
client = OpenAI(base_url="https://openrouter.ai/api/v1",api_key=stringValue)

print(Fore.BLUE+"Now AI is bringing the response please be patient"+Fore.RESET)
completion = client.chat.completions.create(
     model="deepseek/deepseek-r1:free",
     messages=[
       {
         "role": "user",
         "content": "2 sentence answer Is RAG based apps are AI apps?"  
       }
     ]
   )

print(Fore.GREEN+completion.choices[0].message.content+Fore.RESET)