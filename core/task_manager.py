from modules.system_control import handle_system
from modules.file_manager import handle_file
from core.command_parser import parse_llm_response

def execute_task(llm_response):
    task = parse_llm_response(llm_response)

    action = task.get("action")

    if action == "system":
        return handle_system(task)

    elif action == "file":
        return handle_file(task)

    elif action == "chat":
        return task.get("message")

    else:
        return "Task not recognized."