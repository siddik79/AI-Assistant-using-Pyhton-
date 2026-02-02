🎧 Python Voice Assistant

A lightweight voice-controlled assistant built in Python that responds to spoken commands and performs common tasks like opening websites, fetching information, telling jokes, and sending emails using speech recognition and text-to-speech.

✨ What This Assistant Can Do

🎙️ Listen and interpret voice commands

🔊 Respond using text-to-speech (pyttsx3)

🌍 Open popular websites (Google, YouTube, etc.)

📚 Retrieve short summaries from Wikipedia

🕒 Announce the current system time

📩 Send emails using SMTP

😄 Crack random jokes

➗ Handle simple calculations

💬 Answer basic conversational questions

🚪 Exit smoothly when instructed

🛠️ Technologies & Libraries

Python 3

pyttsx3 – Voice output

speech_recognition – Voice input

datetime – Time-related functions

wikipedia – Information lookup

webbrowser – Browser control

smtplib – Email service

pyjokes – Joke generator

os, random – Utility operations

📁 File Structure
Source code.py   # Main application file
README.md        # Project documentation

⚙️ Installation Guide

Clone the repository or download the source files.

Install required dependencies:

pip install pyttsx3 SpeechRecognition wikipedia pyjokes


Microphone support requires pyaudio
(Windows users can install it using):

pip install pipwin
pipwin install pyaudio


If using the email feature, update your Gmail credentials inside the code:

server.login('your_email@gmail.com', 'your_password')

▶️ How to Run

Start the assistant by running:

python "Source code.py"


Example voice commands:

“Open Google”

“Tell me the time”

“Search Python on Wikipedia”

“Tell a joke”

“Send an email”

“Exit”

⚠️ Important Notes

A working microphone is required.

Gmail email sending may need App Passwords or security settings enabled.

The assistant runs continuously until the exit command is given.

This project is intended for learning and demonstration, not production use.

📄 License

Open for educational use and experimentation.
