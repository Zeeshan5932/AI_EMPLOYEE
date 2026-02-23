import random

from modules.system_control import handle_system
from modules.file_manager import handle_file
from modules.browser_automation import handle_browser
from modules.email_sender import handle_email
from modules.document_creator import handle_document
from modules.scheduler import handle_scheduler
from modules.data_analyzer import handle_data

from core.command_parser import parse_llm_response


# 🔹 Smart personality responses
confirmations = [
    "Yes sir, executing your command.",
    "Understood. Processing now.",
    "Right away sir.",
    "On it sir.",
    "Working on your request."
]

completions = [
    "Task completed successfully.",
    "Your request has been fulfilled.",
    "Execution finished.",
    "Done sir."
]


def execute_task(llm_response, gui=None, speaker=None):
    tasks = parse_llm_response(llm_response)

    results = []

    for task in tasks:
        action = task.get("action")

        # 🔹 If normal chat, just return response
        if action == "chat":
            return task.get("message")

        # 🔹 Pre-execution confirmation
        if speaker:
            speaker(random.choice(confirmations))

        if gui:
            gui.update_status("Executing Task...")

        # 🔹 Execute based on action
        if action == "system":
            result = handle_system(task)

        elif action == "file":
            result = handle_file(task)

        elif action == "browser":
            result = handle_browser(task)

        elif action == "email":
            result = handle_email(task)

        elif action == "document":
            result = handle_document(task)

        elif action == "schedule":
            result = handle_scheduler(task)

        elif action == "data":
            result = handle_data(task)

        else:
            result = "Task not recognized."

        results.append(result)

        # 🔹 Completion message
        if speaker:
            speaker(random.choice(completions))

        if gui:
            gui.update_status("Task Completed")

    return " ".join(results)