import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import requests

WAKE_WORD = "jarvis"   # say: "Hey Jarvis"

# -------------------------
# Text-to-Speech
# -------------------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# -------------------------
# Listen function
# -------------------------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio).lower()
        print("You:", text)
        return text
    except:
        return ""

# -------------------------
# Optional AI call
# -------------------------
def ask_ai(prompt):
    api_key = os.getenv("AI_API_KEY")
    if not api_key:
        return "AI key not configured."

    try:
        res = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4.1-mini",
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=20
        )
        if res.status_code == 200:
            return res.json()["choices"][0]["message"]["content"]
    except:
        pass

    return "Could not reach AI."

# -------------------------
# Command handler
# -------------------------
def handle_command(command):

    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "search" in command:
        q = command.replace("search", "")
        speak(f"Searching {q}")
        webbrowser.open(f"https://google.com/search?q={q}")

    elif "ask ai" in command:
        q = command.replace("ask ai", "")
        speak("Thinking...")
        speak(ask_ai(q))

    elif "sleep" in command or "stop listening" in command:
        speak("Going back to sleep.")
        return False

    else:
        speak("Command not recognized.")

    return True

# -------------------------
# Main Wake Loop
# -------------------------
def main():

    speak("Assistant ready. Say Jarvis to wake me.")

    while True:
        text = listen()

        # WAIT FOR WAKE WORD
        if WAKE_WORD in text:
            speak("Yes?")

            # After wake word, listen for commands
            active = True
            while active:
                cmd = listen()
                if cmd:
                    active = handle_command(cmd)

if __name__ == "__main__":
    main()
