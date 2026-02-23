from core.listener import listen_command
from core.speaker import speak
from core.brain_router import process_command
from core.task_manager import execute_task
from core.avatar_gui import AvatarGUI
import threading


gui = AvatarGUI()


def main_loop():
    gui.update_status("AI Active")

    speak("AI Employee Activated")

    while True:
        gui.update_status("Listening...")
        user_input = listen_command()

        if not user_input:
            continue

        gui.add_message("You", user_input)

        if user_input.lower() in ["exit", "quit", "stop"]:
            speak("Shutting down.")
            break

        gui.update_status("Thinking...")
        task_data = process_command(user_input)

        gui.update_status("Executing...")
        result = execute_task(task_data, gui=gui, speaker=speak)

        gui.add_message("AI", result)

        gui.update_status("Speaking...")
        speak(result)

        gui.update_status("Idle")


if __name__ == "__main__":
    threading.Thread(target=main_loop).start()
    gui.run()