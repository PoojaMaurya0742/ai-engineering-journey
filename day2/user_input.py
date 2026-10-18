import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("Groq_API_Key")
if not my_api_key:
    raise ValueError("Groq_API_Key not found ")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"
role="user"
prompt = input("Ask me anything: ")

message={
    "role":role,
    "content":prompt,
}

messages=[message]

response=client.chat.completions.create(
    model=model,
    messages=messages
    )

answer=response.choices[0].message.content

print("\nAI Response:")
print(answer)