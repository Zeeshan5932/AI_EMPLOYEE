import subprocess
import os
import pyautogui
import time


def handle_system(task):
    task_type = task.get("type")

    try:
        # 🔹 OPEN APPLICATION
        if task_type == "open_app":
            app = task.get("app")

            # Better handling for common apps
            if app.lower() == "notepad":
                subprocess.Popen("notepad")
            elif app.lower() == "chrome":
                subprocess.Popen("start chrome", shell=True)
            else:
                subprocess.Popen(app, shell=True)

            return f"Opening {app}"

        # 🔹 TYPE TEXT IN CURRENT WINDOW
        elif task_type == "type_text":
            text = task.get("text", "")

            time.sleep(1)  # wait for window focus
            pyautogui.write(text, interval=0.05)

            return f"Typed: {text}"

        # 🔹 PRESS KEY
        elif task_type == "press_key":
            key = task.get("key")
            pyautogui.press(key)
            return f"Pressed {key}"

        # 🔹 HOTKEY (like ctrl+s)
        elif task_type == "hotkey":
            keys = task.get("keys", [])
            pyautogui.hotkey(*keys)
            return f"Pressed {' + '.join(keys)}"

        # 🔹 TAKE SCREENSHOT
        elif task_type == "screenshot":
            file = "screenshot.png"
            pyautogui.screenshot(file)
            return f"Screenshot saved as {file}"

        # 🔹 SHUTDOWN
        elif task_type == "shutdown":
            os.system("shutdown /s /t 1")
            return "Shutting down system"

        # 🔹 RESTART
        elif task_type == "restart":
            os.system("shutdown /r /t 1")
            return "Restarting system"

        return "System command not supported"

    except Exception as e:
        return f"System error: {str(e)}"