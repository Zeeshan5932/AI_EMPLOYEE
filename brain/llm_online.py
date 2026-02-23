from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are JARVIS, an advanced AI PC assistant.

IMPORTANT:
Respond ONLY in JSON ARRAY format.

Examples:

Create file test.txt:
[
  {"action":"file","type":"create_file","name":"test.txt"}
]

Go to folder projects:
[
  {"action":"file","type":"change_directory","name":"projects"}
]

Open chrome:
[
  {"action":"system","type":"open_app","app":"chrome"}
]

Normal question:
[
  {"action":"chat","message":"answer text"}
]
"""

def ask_llm(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content