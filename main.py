from core.listener import listen_command
from core.speaker import speak
from core.brain_router import process_command
from core.task_manager import execute_task


def main():
    speak("AI Employee Activated")

    while True:
        user_input = listen_command()

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit", "stop"]:
            speak("Shutting down. Goodbye.")
            break

        task_data = process_command(user_input)
        result = execute_task(task_data)

        if result:
            speak(result)


if __name__ == "__main__":
    main()