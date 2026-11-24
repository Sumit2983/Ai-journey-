import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set. Apt not fetched.")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"
role = "user"
prompt = "Suggest me a name for my profile which is unique and catchy. Suggest only one name starts with A"

message_system ={
    "role": "system",
    "content": "You are a brand manager who suggest names for different profiles and brands "

}

message = {
    "role": role,
    "content": prompt
}

messages = [message_system, message]

# default temperature is 0. Range of tempreature is form 0 to 2.

response = client.chat.completions.create(model=model, messages=messages, temperature = 2)
# print(response)  # choices and usage are important in this answer given 
answer = response.choices[0].message.content
print("Response:", answer)
