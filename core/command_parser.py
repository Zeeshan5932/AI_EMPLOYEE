import json

def parse_llm_response(response_text):
    try:
        return json.loads(response_text)
    except:
        return {"action": "chat", "message": response_text}