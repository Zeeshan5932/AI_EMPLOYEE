import subprocess
import os
import pyautogui


def handle_system(task):
    task_type = task.get("type")

    if task_type == "open_app":
        app = task.get("app")
        subprocess.Popen(app)
        return f"Opening {app}"

    elif task_type == "shutdown":
        os.system("shutdown /s /t 1")
        return "Shutting down system"

    elif task_type == "restart":
        os.system("shutdown /r /t 1")
        return "Restarting system"

    elif task_type == "screenshot":
        file = "screenshot.png"
        pyautogui.screenshot(file)
        return "Screenshot taken"

    return "System command not supported"