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
prompt = "waht was the previous response in short "

message = {
    "role": role,
    "content": prompt
}

messages = [message]

response = client.chat.completions.create(model=model, messages=messages)
print(response)  # choices and usage are important in this answer given 
answer = response.choices[0].message.content
print("Response:", answer)
