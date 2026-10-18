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
prompt1="Hi!"
prompt2="explain machine learning in simple terms"
prompt3="explain the process of LLMs ,how they are trained and how they work in simple terms"

prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:
    message={
        "role":role,
        "content":prompt
    }
    
    
    messages=[message]

    response=client.chat.completions.create(
        model=model, 
        messages=messages
        )

    usage = response.usage
    print(f"Prompt:{prompt} -->Your Tokens: {usage.prompt_tokens} Completion Tokens: {usage.completion_tokens} Total Tokens: {usage.total_tokens}")
