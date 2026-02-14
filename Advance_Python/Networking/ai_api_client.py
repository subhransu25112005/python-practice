import os
import requests
import json

# -------------------------------------------------
# 1️⃣ Load API key securely
# -------------------------------------------------
API_KEY = os.getenv("AI_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Set AI_API_KEY environment variable.")

# -------------------------------------------------
# 2️⃣ API endpoint (OpenAI-compatible example)
# Replace with your provider endpoint if needed
# -------------------------------------------------
API_URL = "https://api.openai.com/v1/chat/completions"

# -------------------------------------------------
# 3️⃣ Function to call AI
# -------------------------------------------------
def ask_ai(prompt: str):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4.1-mini",   # change if needed
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)

        if response.status_code != 200:
            print("❌ API Error:", response.status_code)
            print(response.text)
            return None

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        print("❌ Network error:", e)
        return None


# -------------------------------------------------
# 4️⃣ CLI interaction loop
# -------------------------------------------------
def main():
    print("\n===== AI API CLIENT =====")
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("You: ")

        if prompt.lower() == "exit":
            break

        reply = ask_ai(prompt)

        if reply:
            print("\nAI:", reply, "\n")


# -------------------------------------------------
if __name__ == "__main__":
    main()
