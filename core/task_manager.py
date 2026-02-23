from modules.system_control import handle_system
from modules.file_manager import handle_file
from modules.browser_automation import handle_browser
from modules.email_sender import handle_email
from modules.document_creator import handle_document
from modules.scheduler import handle_scheduler
from modules.data_analyzer import handle_data

from core.command_parser import parse_llm_response


def execute_task(llm_response):
    tasks = parse_llm_response(llm_response)

    results = []

    for task in tasks:
        action = task.get("action")

        if action == "system":
            results.append(handle_system(task))

        elif action == "file":
            results.append(handle_file(task))

        elif action == "browser":
            results.append(handle_browser(task))

        elif action == "email":
            results.append(handle_email(task))

        elif action == "document":
            results.append(handle_document(task))

        elif action == "schedule":
            results.append(handle_scheduler(task))

        elif action == "data":
            results.append(handle_data(task))

        elif action == "chat":
            results.append(task.get("message"))

    return " ".join(results)