import json

def parse_llm_response(response_text):
    try:
        data = json.loads(response_text)

        if isinstance(data, list):
            return data
        else:
            return [data]

    except:
        return [{"action": "chat", "message": response_text}]