import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

engine = pyttsx3.init()

# ...

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# ...

def take_query():
    # ...

    while True:
        # ...

        elif "from wikipedia" in query or "wikipedia" in query:
            speak("Checking Wikipedia. Please wait.")
            query = query.replace("wikipedia", "")

            try:
                result = wikipedia.summary(query, sentences=4)
                speak("According to Wikipedia:")
                speak(result)
                
                # Listen for a 'stop' command while speaking
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Listening for 'stop' command...")
                    audio = r.listen(source)
                    try:
                        stop_command = r.recognize_google(audio, language='en-in')
                        if "stop" in stop_command.lower():
                            speak("Stopping.")
                            continue  # Continue listening for the next command
                    except sr.UnknownValueError:
                        pass  # Continue with normal operation if no stop command is heard
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results. Please specify your query.")

        # ...

if __name__ == '__main__':
    take_query()
