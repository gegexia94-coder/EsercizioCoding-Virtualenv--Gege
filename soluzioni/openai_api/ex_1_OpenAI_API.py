import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

testo = "Questa sedia in legno ha una seduta comoda e un design moderno."

response = client.chat.completions.create(
    model="gpt-5.5",
    messages=[
        {"role": "system", "content": "Traduci dall'italiano all'inglese e dall'inglese all'italiano. Rispondi solo con la traduzione."},
        {"role": "user", "content": testo}
    ]
)

print(response.choices[0].message.content)