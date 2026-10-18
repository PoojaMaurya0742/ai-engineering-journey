
import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()
my_api_key = os.getenv("Groq_API_Key")

if not my_api_key:
    raise ValueError("Groq_API_Key not found")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"

# 1. Define the output structure
class Ticket(BaseModel):
    name: str
    email: str
    phone_number: str
    address: str
    issue: str

# 2. Generate schema
schema = Ticket.model_json_schema()

# 3. JSON response format
response_format = {"type": "json_object"}

# 4. System prompt
system_prompt = f"""
Extract customer information from the ticket.
Return valid JSON matching this schema:
{schema}

Extract name, email, phone_number, address, and issue.
Do not invent missing information.
"""

message_system = {
    "role": "system",
    "content": system_prompt
}

# 5. Customer input
text = """
Hello my name is Pooja, I have an iPhone which is not working
at all. My address is Mumbai, my email is abc@gmail.com,
my contact number is 4416578454.
"""

prompt = f"""
Extract the following information from this customer ticket:
{text}
"""

message = {
    "role": "user",
    "content": prompt
}

messages = [message_system, message]

# 6. Call the API
response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format
)

# 7. Get the JSON response
result = response.choices[0].message.content
print("Raw JSON:")
print(result)

# 8. Validate and extract each field
ticket = Ticket.model_validate_json(result)

print("\n--- Extracted Information ---")
print("Name:", ticket.name)
print("Email:", ticket.email)
print("Phone Number:", ticket.phone_number)
print("Address:", ticket.address)
print("Issue:", ticket.issue)
