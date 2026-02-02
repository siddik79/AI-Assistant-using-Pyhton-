import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import random

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to speak audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to recognize voice commands
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query

# Function to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Replace with your Gmail credentials
    server.login('your_email@gmail.com', 'your_password')
    server.sendmail('your_email@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    speak("Initializing Voice Assistant...")
    while True:
        query = takeCommand().lower()
        command_executed = False  # Flag to track if a valid command was executed

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            command_executed = True

        elif 'open youtube' in query:
            speak("Here you go to Youtube")
            webbrowser.open("youtube.com")
            command_executed = True

        elif 'open google' in query:
            speak("Here you go to Google")
            webbrowser.open("google.com")
            command_executed = True

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" the time is {strTime}")
            command_executed = True

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Enter the receiver email address")
                to = input()  # Replace with actual email address if needed
                sendEmail(to, content)
                speak("Email has been sent!")
                command_executed = True
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

       

        elif 'open code' in query:
            code_path = "D:\matrix.cpp"  # Replace with VS Code path
            os.startfile(code_path)
            command_executed = True

        elif 'how are you' in query:
            responses = ["I am functioning perfectly, thank you!", "I'm great, how can I assist you?", "Feeling awesome!"]
            speak(random.choice(responses))
            command_executed = True

        elif 'who are you' in query:
            speak("I am your Assistant")
            command_executed = True

        elif 'joke' in query:
            speak("Sure, here's a joke for you")
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
            command_executed = True

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(query)
            command_executed = True

        elif 'calculate' in query:
            try:
                query = query.replace("calculate", "")
                result = eval(query)
                speak(f"The result of {query} is {result}")
                command_executed = True
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't calculate that")

        elif 'exit' in query:
            speak("Exiting the Voice Assistant, See You soon.")
            break

        # If no valid command executed, say the message only once
        if not command_executed:
            speak("Sorry, I didn't catch that. Can you please repeat?")
