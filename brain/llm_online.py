from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are an AI PC controller.

Convert user commands into JSON format.

Examples:

Open chrome →
{"action":"system","type":"open_app","app":"chrome"}

Create folder test →
{"action":"file","type":"create_folder","name":"test"}

If normal chat →
{"action":"chat","message":"response text"}
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