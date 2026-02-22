def classify_intent(text):
    if "open" in text:
        return "system"
    return "chat"