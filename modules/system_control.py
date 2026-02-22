import subprocess
import os

def handle_system(task):
    task_type = task.get("type")

    if task_type == "open_app":
        app = task.get("app")

        try:
            subprocess.Popen(app)
            return f"Opening {app}"
        except:
            return "Could not open application."

    return "System task not supported yet."