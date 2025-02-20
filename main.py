from dotenv import load_dotenv
from openai import OpenAI
from colorama import Fore
import warnings


warnings.filterwarnings("ignore")

# LOAD ENV VARIABLES
load_dotenv()

# Load the model
client = OpenAI()

# Define a request
print(Fore.GREEN+"I have made it again working, Hurrahh...")


completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "programmer", "content": "You are a helpful assistant."},
    {"role": "user", "content": "can you tell me why we use RAG in AI?"}
  ]
)

print(completion.choices[0].message.content)