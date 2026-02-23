# import speech_recognition as sr


# def listen_command():
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)

#     try:
#         command = recognizer.recognize_google(audio)
#         print("You:", command)
#         return command.lower()

#     except sr.UnknownValueError:
#         print("Could not understand audio")
#         return None

#     except sr.RequestError:
#         print("Speech service unavailable")
#         return None



import speech_recognition as sr
import config

recognizer = sr.Recognizer()
mic = sr.Microphone()


def listen_command():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio).lower()
        print("Heard:", text)

        if config.WAKE_WORD.lower() in text:
            command = text.replace(config.WAKE_WORD.lower(), "").strip()

            if command == "":
                return None

            return command

        return None

    except:
        return None