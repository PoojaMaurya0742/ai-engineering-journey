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
prompt="Suggest a name for a clothing brand?"

#SYSTEM PROMPT
message_system={
    "role":"system",
    "content":"You are a Brand Manager who suggest name for my clothing company, name should be in one word,suggest me only 1 name. "
}
message={
    "role":role,
    "content":prompt
}

messages=[message_system, message]
#Temperature is a parameter that controls the randomness of the model's output. A higher temperature (e.g., 2) will make the output more random and creative, while a lower temperature (e.g., 0.2) will make it more focused and deterministic.by Deault is 0 if not specified.
response=client.chat.completions.create(
    model=model, 
    messages=messages,
    temperature=0
)

print(response.choices[0].message.content)