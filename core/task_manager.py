from modules.system_control import handle_system
from modules.file_manager import handle_file
from modules.browser_automation import handle_browser
from modules.email_sender import handle_email
from modules.document_creator import handle_document
from modules.scheduler import handle_scheduler
from modules.data_analyzer import handle_data

from core.command_parser import parse_llm_response


def execute_task(llm_response):
    task = parse_llm_response(llm_response)

    action = task.get("action")

    if action == "system":
        return handle_system(task)

    elif action == "file":
        return handle_file(task)

    elif action == "browser":
        return handle_browser(task)

    elif action == "email":
        return handle_email(task)

    elif action == "document":
        return handle_document(task)

    elif action == "schedule":
        return handle_scheduler(task)

    elif action == "data":
        return handle_data(task)

    elif action == "chat":
        return task.get("message")

    else:
        return "Task not recognized."