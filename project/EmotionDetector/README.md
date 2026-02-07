🧠 Emotion & Scripture Insight System (Offline)
📌 Project Overview

The Emotion & Scripture Insight System is a Python-based application that analyzes a user’s emotional state through a 20-question psychological MCQ test and provides authentic scripture-based guidance from the Bhagavad Gita.

To ensure reliability, ethical integrity, and stability, the system is designed to work fully offline, using a pre-verified scripture dataset instead of live APIs.

🎯 Objectives

Analyze emotional patterns using psychological MCQs

Identify the dominant emotional state

Provide authentic Bhagavad Gita verses related to that emotion

Ensure zero AI-generated advice

Avoid dependency on unstable public APIs

⚙️ Key Features

✅ 20 advanced psychological MCQs

✅ Emotion analysis with dominant & secondary traits

✅ Fully offline scripture retrieval

✅ Authentic, pre-verified Bhagavad Gita verses

✅ Multi-page interactive UI using Streamlit

✅ Restartable test flow

❌ No internet required

❌ No external APIs

❌ No generated or paraphrased spiritual advice

🧩 Project Architecture
User → MCQ Test → Emotion Analysis → Scripture Mapping → Result Display


MCQs identify psychological tendencies

Logic engine computes dominant emotion

Offline scripture database maps emotion → verse

UI displays source, reference, and original text

📁 Final File Structure
EmotionDetector/
│
├── app.py              # Main Streamlit application
├── logic.py            # Emotion analysis engine
├── questions.py        # 20 psychological MCQs
├── gita_fallback.py    # Offline Bhagavad Gita verses
├── requirements.txt    # Dependencies

🛠️ Technologies Used

Python 3

Streamlit (UI framework)

📦 Installation & Running
1️⃣ Install dependency
pip install streamlit

2️⃣ Run the application
streamlit run app.py

3️⃣ Open browser
http://localhost:8501

📖 Scripture Source

Bhagavad Gita (offline, pre-verified verses)

Verses are standard translations commonly used in academic references

Each emotional state is mapped to a specific chapter and verse

⚖️ Ethical & Academic Integrity

The system does NOT generate advice

The system does NOT modify scripture

The system does NOT interpret religious meaning

Only original verse text is displayed

Offline design ensures consistency during demos & evaluations

“This system retrieves scripture from an authenticated offline dataset to guarantee reliability without generating or altering spiritual content.”

🎓 Use Cases

Academic mini / major projects

Hackathons

Psychology & self-awareness tools

Ethical AI demonstrations

Offline demos (no internet dependency)

🚀 Future Enhancements

Add Bible offline verses

Hindi / English language toggle

PDF export of results

Emotional trend visualization

Mobile-friendly UI
Cheak it:
https://emotiondct.streamlit.app/

👤 Author

Subhranshu Nanda
Computer Science & Engineering Student

📜 License

This project is intended for educational and academic use only.