from core.listener import listen_command
from core.speaker import speak
from core.brain_router import process_command
from core.task_manager import execute_task
from core.avatar_gui import AvatarGUI
import threading
import datetime
import random

gui = AvatarGUI()


def get_greeting():
    hour = datetime.datetime.now().hour

    if hour < 12:
        return "Good morning sir."
    elif hour < 18:
        return "Good afternoon sir."
    else:
        return "Good evening sir."


def main_loop():
    gui.update_status("AI Active")

    greeting = get_greeting()
    speak(f"{greeting} JARVIS online and ready.")
    gui.add_message("JARVIS", f"{greeting} JARVIS online and ready.")

    while True:
        gui.update_status("Listening...")
        user_input = listen_command()

        if not user_input:
            continue

        gui.add_message("You", user_input)

        if user_input.lower() in ["exit", "quit", "stop"]:
            speak("Shutting down. Goodbye sir.")
            break

        gui.update_status("Thinking...")
        task_data = process_command(user_input)

        gui.update_status("Executing...")
        result = execute_task(task_data, gui=gui, speaker=speak)

        if result:
            gui.add_message("JARVIS", result)

        gui.update_status("Idle")


if __name__ == "__main__":
    threading.Thread(target=main_loop, daemon=True).start()
    gui.run()