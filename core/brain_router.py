from brain.llm_online import ask_llm

def process_command(user_input):
    response = ask_llm(user_input)
    return response