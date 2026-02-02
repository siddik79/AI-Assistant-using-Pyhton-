# 🎙️ Voice Assistant in Python

A simple **Python-based voice assistant** that can perform everyday tasks such as opening websites, searching Wikipedia, telling jokes, sending emails, and more using **speech recognition** and **text-to-speech**.

---

## 🚀 Features

* 🔊 **Speech Recognition** (understands voice commands)
* 🗣️ **Text-to-Speech** responses using `pyttsx3`
* 🌐 Open websites like YouTube, Google
* 📖 Fetch summaries from **Wikipedia**
* ⏰ Tell the current time
* 📧 Send emails via Gmail SMTP
* 🤖 Tell random jokes (`pyjokes`)
* 🧮 Perform basic calculations
* 💬 Fun interactions (“Who are you?”, “How are you?”)
* ❌ Exit gracefully on command

---

## 🧰 Libraries Used

* `pyttsx3` – Text-to-Speech
* `speech_recognition` – Speech to Text
* `datetime` – Get system time
* `wikipedia` – Fetch Wikipedia summaries
* `webbrowser` – Open websites
* `smtplib` – Send emails
* `pyjokes` – Generate jokes
* `os` – Open files/programs
* `random` – Randomized responses

---

## 📂 Project Structure

```
Source code.py   # Main Python script
README.md        # Documentation
```

---

## ⚙️ Setup & Installation

1. Clone the repository or download the code.
2. Install required libraries:

```bash
pip install pyttsx3 SpeechRecognition wikipedia pyjokes
```

*(Ensure you also have `pyaudio` installed for microphone input. On Windows use `pip install pipwin && pipwin install pyaudio`.)*

3. Replace placeholder Gmail credentials in `sendEmail()` with your own if using the email feature:

```python
server.login('your_email@gmail.com', 'your_password')
```

---

## ▶️ Usage

Run the assistant with:

```bash
python "Source code.py"
```

Speak commands like:

* "Open YouTube"
* "Search Python programming"
* "What time is it?"
* "Tell me a joke"
* "Send email"
* "Exit"

---

## ⚠️ Notes

* You need an active microphone for speech recognition.
* Email functionality requires **less secure app access enabled** on Gmail (or an App Password if 2FA is enabled).
* The assistant runs continuously in a loop until you say **“exit”**.

---

## 📜 License

This project is for **educational purposes** only. Feel free to modify and extend.

---

